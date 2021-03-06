#from compredict.client import api
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)



def test():
        import os,sys,inspect
        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        parentdir = os.path.dirname(currentdir)
        sys.path.insert(0,parentdir)

        from compredict.client import api
        from compredict.resources import resources
        from time import sleep
        #from environs import Env
        from sys import exit
        import json

        #env = Env()
        #env.read_env()

#        token = env("COMPREDICT_AI_CORE_KEY", "3bd00ee3265f6c06b60344802ab85cbaf20426b2")
#        callback_url = env("COMPREDICT_AI_CORE_CALLBACK", None)
#        fail_on_error = env("COMPREDICT_AI_CORE_FAIL_ON_ERROR", False)
#        ppk = env("COMPREDICT_AI_CORE_PPK", None)
#        passphrase = env("COMPREDICT_AI_CORE_PASSPHRASE", "")
#        base_url = env("COMPREDICT_AI_CORE_BASE_URL", "https://b.aic.compredict.de/api/v{}")
        token = "3bd00ee3265f6c06b60344802ab85cbaf20426b2"
        base_url = "https://b.aic.compredict.de/api/v{}"

        client = api.get_instance(token=token, callback_url=callback_url, ppk=ppk, passphrase=passphrase,base_url=base_url)
        client.fail_on_error(option=fail_on_error)

        # get a graph
        # algorithm = client.get_algorithm("auto-parameterization")
        # graph = algorithm.get_detailed_graph()
        # new_file = open('auto-parameterization-graph.png', 'wb')
        # shutil.copyfileobj(graph, new_file)
        # graph.close()


        algorithms = client.get_algorithms()

        # Check if the user has algorithms to predict
        if len(algorithms) == 0:
            print("No algorithms to proceed!")
            exit()

        #algorithm = algorithms["base-damage-forecaster"]
        algorithm = algorithms[0]

        #json file test
        data = {}
        with open('base-damage-forecaster.json', 'r') as f:
            data = json.loads(f.read())
            print(data)
        #data = []
        #for line in open('tweets.json', 'r'):
        #    data.append(json.loads(line))

        tmp = algorithm.get_detailed_template()
        tmp.close()  # It is tmp file. close the file to remove it.

        "data = dict()  # data for predictions"

        results = algorithm.run(data, evaluate=False, encrypt=True)

        if isinstance(results, resources.Task):
            print(results.job_id)

            while results.status != results.STATUS_FINISHED:
                print("task is not done yet.. waiting...")
                sleep(15)
                results.update()

            if results.success is True:
                print(results.predictions)
            else:
                print(results.error)

        else:
            print(results.predictions)

#print(test())
