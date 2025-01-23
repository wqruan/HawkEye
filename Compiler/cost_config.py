import re
from collections import defaultdict, deque
import math

#Basic operations, these operations are necessary for one protocol
# share:
# open:
# muls:
# matmuls:

#advance operations, these operations are optional
# TruncPr:
# LTZ:
# Trunc
# Mod2m:
# EQZ:
# SDiv:
# Pow2:
# FPDiv:
# sin:
# cos:
# tan:
# exp2_fx:
# log2_fx:
# sqrt:
# atan:


class Cost(object):
    f = 0
    bit_length = 1
    _security = 1
    n_parties = 2
    computation_security = 1
    cost_dict = defaultdict(lambda: -1)
    cost_dict_func = defaultdict(lambda: -1)
    subcls = None
    @classmethod
    def update_cost(cls):
        for key, value in cls.cost_dict_constasnt_func.items():
            if value.__code__.co_argcount == 5:
                cls.cost_dict[key] = value(cls.bit_length, cls._security, cls.computation_security, cls.f, cls.n_parties)
            else:
                cls.cost_dict[key] = value  
        for key, value in cls.cost_dict_func.items():
            if value.__code__.co_argcount == 5:
                cls.cost_dict[key] = value(cls.bit_length, cls._security,cls.computation_security, cls.f, cls.n_parties)                    
            else:   
                cls.cost_dict[key] = value
        muls = cls.cost_dict['muls'](cls.bit_length, cls._security, cls.computation_security, cls.f, cls.n_parties, cls.program.degree, cls.program.modulus, 1)
        cls.cost_dict["square"] = (0, 0, (muls[0]+muls[2]), (muls[1]+muls[3]))
        
        if cls.program.protocol=="SPDZ":
            cls.cost_dict["randbit"] = (0, 0, (cls.cost_dict['open'][0]+cls.cost_dict['open'][2])*cls.n_parties+\
                (muls[0]+muls[2])*(cls.n_parties-1), \
                    (cls.cost_dict['open'][1]+cls.cost_dict['open'][3])+\
                        (muls[1]+muls[3])*(cls.n_parties-1))            
        elif cls.program.options.ring:
            cls.cost_dict["randbit"] = (0, 0, (cls.cost_dict['share'][0]+cls.cost_dict['share'][2])*cls.n_parties+\
                (muls[0]+muls[2])*(cls.n_parties-1), \
                    (cls.cost_dict['share'][1]+cls.cost_dict['share'][3])+\
                        (muls[1]+muls[3])*(cls.n_parties-1))
        else:
            cls.cost_dict["randbit"] = (0, 0, cls.cost_dict['open'][0], cls.cost_dict['open'][1])     
            cls.cost_dict["dabit"] = (0, 0, cls.cost_dict["randbit"][2] +\
             (cls.cost_dict['share'][0]+cls.cost_dict['share'][2])*cls.n_parties, \
                 cls.cost_dict["randbit"][3]+(cls.cost_dict['share'][0]+cls.cost_dict['share'][2]))
                 
    @classmethod
    def init(cls, program):
        for arg in program.args:
                m = re.match('f([0-9]+)$', arg)
        if m:
                cls.f = int(m.group(1))
        if program.options.ring:
            cls.bit_length = program.bit_length+1
        else:
            cls.bit_length = program.bit_length
        cls._security = cls.bit_length
        cls.computation_security = program.c_security
        cls.n_parties = program.n_parties
        cls.program = program
        cls.update_cost()
        Cost.subcls = cls
    
    @classmethod
    def set_precision(self, precision):
        Cost.f = precision
        Cost.subcls.update_cost()

    cost_dict_constasnt_func = {
        "triple":lambda bit_length, kappa_s ,kapaa, precision, n_parties: (0, 0, bit_length * (bit_length+kapaa), 1), # currently, only for two party
        "sedabit": lambda bit_length,  kappa_s ,kapaa, precision, n_parties, len: (0, 0, 0, 0),
        "edabit": lambda bit_length,  kappa_s ,kapaa, precision, n_parties, len: (0, 0, 0, 0),
        "dabit": lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (0, 0, 0, 0), #done
        "shufflegen": lambda bit_length,  kappa_s ,kapaa, precision, n_parties, size: (0, 0, 0, 0),
        "shuffleapply": lambda bit_length,  kappa_s ,kapaa, precision, n_parties, size, record_size: (0, 1, 0, 0),
        "randbit": lambda bit_length,  kappa_s , kapaa, precision, n_parties: (0, 0, 1, 1), #done
    }
    @classmethod
    def get_cost(self, name):
        return self.cost_dict[name]


class ABY3(Cost): #done
    cost_dict_func = {
        "share": lambda bit_length,  kappa_s , kapaa, precision, n_parties: (bit_length*3, 1, 0, 0),
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*3, 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (size*bit_length*3, 1, 0, 0),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*r*bit_length*3, 1, 0, 0),
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: (bit_length, 1, 0, 0),
        "LTZ": lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*9, math.log2(bit_length)+2, 0, 0),
        # "trunc": lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length, 1, 0, 0),
        # "bit_share":lambda bit_length, kappa_s , kapaa, precision, n_parties: (3, 1, 0, 0),
        # "ands":lambda bit_length, kappa_s , kapaa, precision, n_parties: (3, 1, 0, 0)
   }

class DeepMPC(Cost): #done
    cost_dict_func = {
        "share": lambda bit_length,  kappa_s , kapaa, precision, n_parties: (bit_length, 1, 0, 0),
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*3, 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (size*bit_length*3, 1, 0, 0),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*r*bit_length*3, 1, 0, 0),
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: (bit_length*8, 1, 0, 0),
        "LTZ": lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*10.375, math.log2(bit_length)+2, 0, 0),
        # "trunc": lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length, 1, 0, 0),
        # "bit_share":lambda bit_length, kappa_s , kapaa, precision, n_parties: (3, 1, 0, 0),
        # "ands":lambda bit_length, kappa_s , kapaa, precision, n_parties: (3, 1, 0, 0)
   }

class SecureML(Cost): #done
    cost_dict_func = {
        "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (0, 0, 0, 0),
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*2, 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (size*bit_length*4, 1, size*bit_length * (bit_length+kapaa), 1),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*q*bit_length*2+p*r*bit_length*2, 1, p*q*r*bit_length * (bit_length+kapaa), 1),
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: (0, 0, 0, 0)
   }

class ABY(Cost):
    cost_dict_func = {
        "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (0, 0, 0, 0),
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*2, 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (size*bit_length*4, 1, size*bit_length*(2*kapaa+bit_length+1), 2),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*q*r*bit_length*4, 1, p*q*r*bit_length*(2*kapaa+bit_length+1), 2),
        "trunc": lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (0, 0, 0, 0),
        "TruncPr" : lambda bit_length,  kappa_s ,kapaa, precision, n_parties, knownmsb: (0, 0, 0, 0),
        "LTZ": lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (bit_length*kapaa*7+(bit_length**2+bit_length)/2, 4, bit_length*kapaa*5, 2),
   }
class MPCFormer(Cost):
    cost_dict_func = {
    "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (0, 0, 0, 0),
    "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*2, 1, 0, 0),
    "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (size*bit_length*4, 1, size*bit_length, 3),
    "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: ((p*q + q*r)*bit_length*2, 1, p*r*bit_length, 3),
    "TruncPr": lambda bit_length,  kappa_s ,kapaa, precision, n_parties, knownmsb: (0, 0, 0, 0),
    "exp_fx":lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*16, 8, bit_length*8, 24),
    "LTZ":lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (bit_length*54, 8, bit_length*14, 24),
    "EQZ":lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (bit_length*26, 7, bit_length*7, 21),
    "Reciprocal":lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (bit_length*138, 38, 44*bit_length, 114)
}
    
def compute_subshape(p, q, r, degree):
    cpu_price = 1.0
    bandwidth_price = 1000.0
    res = [0, 0, 0]
    blk = [0, 0, 0]
    min_cost = 2**60

    for d0 in range(1, min(degree, p+1)):
        blk[0] = math.ceil(p*1.0/d0)
        d1 = 1
        while d1 <= q:
            if d0*d1 > degree:
                break
            blk[1] = math.ceil(q*1.0/d1)
            d2 = min(r, math.ceil(degree*1.0/d0/d1))
            blk[2] = math.ceil(r*1.0/d2)
            sent_ct = min(blk[0], blk[2])*blk[1]
            response_ct = math.ceil(blk[0] * blk[2]*1.0/d1);
            num_automorph = math.ceil(p*1.0*r/ degree) * d1
            num_ct_mul = blk[0] * blk[1] * blk[2]
            cost = (sent_ct + response_ct) * bandwidth_price +\
                    num_automorph * cpu_price + num_ct_mul * cpu_price / 10.0
            if (cost <= min_cost):
                min_cost = cost;
                res = [d0, d1, d2]
                
            d1 = d1 * 2;
    blk = [math.ceil(p/res[0]), math.ceil(q/res[1]), math.ceil(r/res[2])]
    return min(blk[0], blk[2]) * blk[1],  math.ceil(blk[0] * blk[2]*1.0/res[1])

class Cheetah(Cost):
    cost_dict_func = {
    "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (0, 0, 0, 0),
    "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*2, 1, 0, 0),
    "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: ( math.ceil(size/degree)*(degree*sum(modulus[0:-1])+degree*sum(modulus[0:-2])),2, 0, 0),
    "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (2*(compute_subshape(p, q, r, degree)[0]*degree*sum(modulus[0:-1])+(math.ceil(p*r/degree)*degree+compute_subshape(p, q, r, degree)[1]*degree)*sum(modulus[0:-2])), 2, 0, 0),
    "TruncPr" : lambda bit_length,  kappa_s ,kapaa, precision, n_parties, knownmsb: ( precision+4 , 2, 0, 0),
    "LTZ": lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (13*bit_length+1, math.ceil(math.log2(bit_length)), 0, 0),
}  

class CryptoFlow2(Cost):
    cost_dict_func = {
        "share": lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (0, 0, 0, 0),
        "open" : lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (bit_length*2, 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (size*bit_length*(math.ceil((bit_length+1)/2)+kapaa), 2, 0, 0),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (q*r*bit_length*(p*math.ceil((bit_length+1)/2)+kapaa),bit_length/math.ceil(2**24/(p*q*r))*2, 0, 0),
        "LTZ": lambda bit_length, kappa_s , kapaa, precision,  n_parties: ((kapaa+18)*bit_length, math.ceil(math.log2(bit_length)), 0, 0),
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: (kapaa*precision+14*precision + 2*kapaa + 4*bit_length if knownmsb else (kapaa)*(bit_length+2)+19*bit_length+kapaa*precision+14*precision, math.ceil(math.log2(bit_length))+2 if knownmsb else 2*math.ceil(math.log2(bit_length))+4, 0, 0)
   }
class SPDZ(Cost):
    cost_dict_func = {
        "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: ((kappa_s+bit_length)*(n_parties-1), 1, (kappa_s*bit_length+kappa_s**2)*n_parties*(n_parties-1), 3), # offline: Fmac 
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: ((bit_length+kappa_s)*n_parties*(n_parties-1), 1, (kappa_s*bit_length+kappa_s**2)*n_parties*(n_parties-1), 3), #((bit_length+kappas_s)*n_parties)
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (size*(bit_length+kappa_s)*n_parties*(n_parties-1)*2, 1, size*(n_parties*(n_parties-1)*(18*kappa_s*kappa_s+4*bit_length*bit_length+17*bit_length*kappa_s)), 8), #(Fmac+(bit_length+kappas_s)*n_parties)
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*q*r*(bit_length+kappa_s)*n_parties*(n_parties-1)*2, 1, p*q*r*(n_parties*(n_parties-1)*(18*kappa_s*kappa_s+4*bit_length*bit_length+17*bit_length*kappa_s)), 8), #pqr(Fmac+(bit_length+kappas_s)*n_parties)
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: ((bit_length+kappa_s)*n_parties*(n_parties-1), 1, bit_length*((kappa_s+bit_length)*(3*n_parties+1)*(n_parties-1)+(kappa_s*bit_length+kappa_s**2)*n_parties*(n_parties-1)*2+n_parties*(n_parties-1)*(18*kappa_s*kappa_s+4*bit_length*bit_length+17*bit_length*kappa_s)), 11)
   }

class BGW(Cost): #done
    cost_dict_func = {
        "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (n_parties-math.floor(n_parties/2)-1, 1, 0, 0),
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (n_parties*math.floor(n_parties/2), 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (n_parties*(n_parties-math.floor(n_parties/2)-1)*size, 1, 0, 0),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*r*n_parties*(n_parties-math.floor(n_parties/2)-1), 1, 0, 0)
        # "trunc": lambda bit_length, kapaa, precision, n_parties: (bit_length*3, 1, 0, 0)
   }

class Falcon(Cost):
    cost_dict_func = {
        "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*3, 1, 0, 0),
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*6, 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size:  (bit_length*6*size, 1, 0, 0),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*r*bit_length*6, 1, 0, 0),
        "LTZ": lambda bit_length, kappa_s , kapaa, precision,  n_parties: (24*bit_length, math.log2(bit_length)+5, 3*bit_length*(bit_length+8+math.log2(bit_length)), math.log2(bit_length)+4+math.log2(bit_length)),
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: (bit_length, 1, bit_length*8+bit_length+bit_length*math.log2(bit_length)+(bit_length-precision)+(bit_length-precision)*math.ceil(math.log2((bit_length-precision))), math.log2(bit_length)+4+math.log2(bit_length)),
        "Pow2":lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*bit_length*(24),  bit_length*(math.log2(bit_length)+5), (3*bit_length*(bit_length+8+math.log2(bit_length)))*bit_length, math.log2(bit_length)+4+math.log2(bit_length)),
        "Reciprocal":lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (bit_length*bit_length*(24) + 36*bit_length, bit_length*(math.log2(bit_length)+5)+5, (3*bit_length*(bit_length+8+math.log2(bit_length)))*bit_length, math.log2(bit_length)+4+math.log2(bit_length)),
   }
class Delphi(Cost):
    cost_dict_func = {
        "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (0, 0, 0, 0),
        "open" : lambda bit_length,  kappa_s ,kapaa, precision, n_parties: (bit_length, 1, 0, 0),
        "muls" : lambda bit_length, kappa_s , kapaa, precision, n_parties, degree, modulus, size: (bit_length, 1, (math.ceil(size/degree)+math.ceil(size/degree))*degree*sum(modulus)*2, 2),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (p*q*bit_length, 1, (math.ceil(p*r/degree)+math.ceil(p*q/degree))*degree*sum(modulus)*2, 2),
        "LTZ": lambda bit_length, kappa_s , kapaa, precision,  n_parties: (148*bit_length, 1, 2370*bit_length, 3),
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: (0, 0, 0, 0),
        "conv2d": lambda bit_length, kappa_s , kapaa, precision, n_parties, batch_size, in_channel, out_channel, inw, inh, outw, outh, kw, kh, stridew, strideh, paddingw, paddingh, groups, degree, modulus: \
            (batch_size*in_channel*inw*inh*bit_length, 1,\
                (batch_size*math.ceil(in_channel*inw*inh/float(degree))*kw*kh*degree*sum(modulus)+math.ceil(batch_size*out_channel*outw*outh/degree)*degree*sum(modulus))*2, 2)
   }
    
def computestepsforsemi2k(p, q, r, bitlength, mem_limit=1024*1024*256):
    if p == 0 or q == 0 or r == 0:
        return p*q +q*r
    if (p*q+q*r)*bitlength/8 < mem_limit:
        return p*q +q*r

    elnum_limit = mem_limit / (bitlength/8)
    q_step = 0
    expected_pr_step =0
    if q > (p+ r) * 8:
        expected_pr_step = p+r
        q_step = max(1, math.ceil(elnum_limit / expected_pr_step))
    elif (p + r) > q * 8: 
        q_step = q;
        expected_pr_step = max(1, math.ceil(elnum_limit / q_step))
    else:
        q_pr_radio =  q*1.0 / (p+r);
        pr_step = math.sqrt(elnum_limit / q_pr_radio)
        q_step = max(1, math.ceil(elnum_limit / pr_step))
        expected_pr_step = max(1, math.ceil(pr_step))

    p_step = max(math.floor(expected_pr_step * p / (p + r)), 1);
    r_step = max(math.floor(expected_pr_step * r / (p + r)), 1);
    print(q_step)
    p_blocks = math.ceil(p*1.0/p_step)
    q_blocks = math.ceil(q*1.0/q_step)
    r_blocks =  math.ceil(r*1.0/r_step)
    res =0
    for i in range(p_blocks):
        for j in range(q_blocks):
            for k in range(r_blocks):
                p_sub = min(p - p_step*i, p_step)
                q_sub = min(q - q_step*j, q_step)
                r_sub = min(r - r_step*k, r_step)
                res += p_sub*q_sub +q_sub*r_sub
    return res
                
    
class Semi2k(Cost): #done, align with secretflow
    cost_dict_func = {
        "share": lambda bit_length, kappa_s , kapaa, precision, n_parties: (0, 0, 0, 0),
        "open" : lambda bit_length, kappa_s , kapaa, precision, n_parties: (bit_length*2, 1, 0, 0),
        "muls" : lambda bit_length,  kappa_s ,kapaa, precision, n_parties, degree, modulus, size: (bit_length*4*size, 1, 0,0),
        "matmuls": lambda bit_length, kappa_s , kapaa, precision, n_parties, p ,q, r, degree, modulus: (2*bit_length*computestepsforsemi2k(p,q,r,bit_length), 1,0,0),
        "TruncPr": lambda bit_length, kappa_s , kapaa, precision, n_parties, knownmsb: (2*bit_length, 1, 0,0),
        "LTZ": lambda bit_length, kappa_s , kapaa, precision, n_parties: (2*(2*bit_length+ 2*(n_parties-1)*(2*bit_length+32)), math.log2(bit_length)+1, 0,0)
   }
protocol_store = {
    "ABY3" : ABY3(),
    "SecureML" : SecureML(),
    "ABY": ABY(),
    # "ABY2.0": ABY2(),
    "Falcon": Falcon(),
    "BGW": BGW(),
    "CryptFlow2": CryptoFlow2(),
    "MPCFormer": MPCFormer(),
    "SPDZ": SPDZ(),
    "Delphi": Delphi(),
    "Cheetah": Cheetah(),
    "SEMI2K": Semi2k(),
    "DeepMPC": DeepMPC()
}

def get_cost_config(name):
    return protocol_store[name]



if __name__ == "__main__":
    print(128*59+4*59)
    print(cryptflow2_cost(32, 7, 128))