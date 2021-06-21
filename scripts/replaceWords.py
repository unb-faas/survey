import sys
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
matches = ("latency measurements","load balancing.","machine learning as a service (mlaas)", "micro service architecture", "microservice ar chitecture","microsoft azure functions", "micro service", "multi clouds", "multicloud", "operating systems", "open whisk","opensource serverless computing frameworks", "auto scaling", "optimisation", "web assembly", "unikernels", "software architectures", "service oriented architectures", "server les computing", "servelress", "platform as a service (paas)", "infrastructure as a service (iaas)", "software as a service (saas)", "function as a service (faas)")
substitute = ("latency measurement","load balancing","machine learning as a service", "microservice architecture", "microservice architecture","microsoft azure function", "microservice", "multi cloud", "multi cloud", "operating system", "openwhisk","open source serverless computing frameworks", "autoscaling", "optimization" , "webassembly", "unikernel", "software architecture","service oriented architecture", "serverless computing", "serverless","platform as a service", "infrastructure as a service", "software as a service", "function as a service")
for idx, term in enumerate(Lines):
    term = term.replace("\n","")
    if term in matches:
        print(substitute[matches.index(term)])
    else:
        print(term)