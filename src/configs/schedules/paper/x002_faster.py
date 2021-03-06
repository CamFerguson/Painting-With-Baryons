import os
from src.configs.schedules.paper.stock import schedule
from src.configs.spectral.spectral_g import g_structure
from src.configs.spectral.spectral_d import d_structure


folder = os.path.basename(os.path.dirname(__file__))
subfolder = os.path.splitext(os.path.basename(__file__))[0]
name = '/' + folder + '/' + subfolder + '/'
schedule['save_dir'] += name

schedule['batch_size'] = 6
schedule['optimizer_params']['perceptual_loss_opts']['percep_lambda'] = 5

g_structure['decode_stack']['filters'][-1]['init_gain'] = 0.25
g_structure['res_blocks']['n_blocks'] = 3

schedule['optimizer_params']['g']['opts']['lr'] = 7.5e-5
schedule['optimizer_params']['d']['opts']['lr'] = 7.5e-5

schedule['optimizer_params']['g']['decay']['opts']['gamma'] = 0.96
schedule['optimizer_params']['d']['decay']['opts']['gamma'] = 0.96

schedule['pseudo_epoch_iters'] = 105
