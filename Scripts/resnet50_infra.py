import subprocess

def runMPL(model, vm = 'Scripts/ring.sh', args = ['-F']):
    try:
        response = subprocess.run([vm, model, *args], capture_output=True, text=True, check=True)
        print(response.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        print(e.stdout)

vm = 'Scripts/ring.sh'
args = ['-F', '-v']

model = "resnet50_base.onnx"
runMPL(model, vm, args)

model = "resnet50_base_105_taso_inference.onnx"
runMPL(model, vm, args)

model = "resnet50_base_105_hawkeye_inference.onnx"
runMPL(model, vm, args)