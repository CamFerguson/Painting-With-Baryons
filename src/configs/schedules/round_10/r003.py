import os

folder = os.path.basename(os.path.dirname(__file__))
subfolder = os.path.splitext(os.path.basename(__file__))[0]
name = '/' + folder + '/' + subfolder + '/'

from src.configs.schedules.round_10.stock import Schedule
from src.configs.resnet.dim256x1 import g_structure
from src.configs.patchgan.dim256x2_70_nobn_nosig import d_structure

schedule = Schedule(name)
schedule['sample_interval'] = 100
schedule['g_optim_opts']['lr'] = 0.002
schedule['d_optim_opts']['lr'] = 0.002

#schedule['debug_plot'] = True
