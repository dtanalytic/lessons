import configparser

if __name__=='__main__':
    
    cfg = configparser.ConfigParser()
    cfg.read('../data/conf.cfg')
    cfg['общая']['параметрN']
