import subprocess
from linenotipy import Line

DEFAULT_ATTRIBUTES = (
    'name',
    'memory.total',
    'memory.free',
    'memory.used',
    'utilization.gpu',
    'utilization.memory'
)

class GPUMonitor2LINE():
  def __init__(self):
    self.gpu_inf = list(dict())
    self.message = ''

  def get_gpu_info(self, nvidia_smi_path='nvidia-smi', keys=DEFAULT_ATTRIBUTES, no_units=True):
    nu_opt = '' if not no_units else ',nounits'
    cmd = '%s --query-gpu=%s --format=csv,noheader%s' % (nvidia_smi_path, ','.join(keys), nu_opt)
    output = subprocess.check_output(cmd, shell=True)
    lines = output.decode().split('\n')
    lines = [ line.strip() for line in lines if line.strip() != '' ]
    
    self.gpu_inf = [ { k: v for k, v in zip(keys, line.split(', ')) } for line in lines ]      
    return

  def line_notify(self):
    line = Line(token='<Your Token>')
    line.post(message=self.message)
    return

  def set_gpu_info_to_message(self):
    self.message = "\n" + "\n\n".join(["\n".join([key+": "+gpu_info[key] for key in gpu_info.keys()]) for gpu_info in self.gpu_inf])
    return

  def set_text_to_message(self, text):
    self.message = text
    return


if __name__ == '__main__':
  # build a GPUMonitor2LINE onject
  gpumonitor2line = GPUMonitor2LINE()
  
  # get current gpu information
  gpumonitor2line.get_gpu_info()

  # set gpu information as string to notify
  gpumonitor2line.set_gpu_info_to_message()
    
  # LINE Notify
  gpumonitor2line.line_notify()
