# Source: https://github.com/anaustinbeing/spark-remove-stopwords/blob/master/removestopwords.py
#from pyspark import SparkContext
#from nltk.corpus import stopwords
#import re
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk
nltk.download('punkt')


#class RemoveStopWords:
#    def __init__(self, name):
#        self.spark = SparkContext('local[3]', name)##

#    def read_RDD(self, path):
#        return self.spark.textFile(path)

#   def filter_words(self, lines):
#        stopwords_list = stopwords.words('english')
#        return lines.flatMap(lambda x: x.split()).filter(lambda x: x.lower() not in stopwords_list).collect()

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        filename=False
    if (filename):
       

        #example_sent = """This is a sample sentence,
        #                showing off the stop words filtration."""
        
        stop_words = set(stopwords.words('english'))
        
        #word_tokens = word_tokenize(example_sent)
        
        #filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
        
        #filtered_sentence = []
        
        #for w in word_tokens:
        #    if w not in stop_words:
        #        filtered_sentence.append(w)
        
        #print(word_tokens)
        #print(filtered_sentence)

        print(stop_words)
       
       
        file1 = open(filename, 'r')
        Lines = file1.readlines()
        customStopWords = ["aaf","abc","ace","acl","aco","add","aes","afm","aft","ago","aid","aim","aka","all","als","amb","amr","amt","and","ant","any","apd","apl","app","ard","are","ark","arm","ars","art","ash","ast","bal","bar","bid","ble","brt","bsp","but","can","cap","cdc","cdg","cdh","cep","cfd","cfp","cfs","clr","cnf","cod","com","cpg","cps","cqs","csp","ctr","cut","cvs","cwl","cxl","daf","dag","dcs","def","des","dht","dig","diy","dlt","dna","dnn","dos","dot","dpn","dsl","dsm","dsp","due","dve","ecc","ecg","edc","end","eon","epc","esp","etc","etl","fdl","fdn","fed","fee","few","ffc","fhe","fin","for","fsa","gas","gci","gcs","gds","gen","get","gig","gis","gle","gnn","got","gps","gsc","gsp","gui","han","har","hdp","hep","hex","hgn","hoc","how","hrv","hue","icn","ict","ids","ifc","igi","iii","ilp","inâ","inc","ini","inp","iop","ios","ipc","irs","isp","its","ity","jar","jct","jhu","jms","jon","key","kit","kpi","lag","lan","lay","lda","leo","let","lex","lip","liu","llc","lot","lsm","ltd","lxc","may","mbs","mcu","mdc","mdp","mec","met","mfc","mgf","mix","mlr","mme","moe","mom","mpc","mps","mri","muc","ndn","nec","nfn","nft","nfv","ngs","nic","nlp","nmr","non","not","npk","npu","nss","ntt","obe","ocr","oee","ofc","ofn","oil","old","one","ooa","osd","osm","osn","oth","our","out","pcs","pdb","pen","per","pi를","pid","pis","pki","pls","pne","poc","pod","pom","pop","pos","ppg","pro","pss","pte","ptt","put","pvt","qch","qoe","qrp","ran","rar","raw","ray","rfs","rid","rms","rnn","rns","rpa","rps","rrt","rss","rtt","rup","san","sau","say","sba","sbi","scc","sda","sdc","sdi","see","set","sev","sgc","sgd","sgs","sgx","sio","sip","six","sla","slo","smp","snf","sno","snp","sns","soa","soc","sod","sol","sqs","srv","srw","ssd","ssg","ssi","sum","svp","tan","tco","ten","tfc","the","tie","tim","tlb","tls","toa","tor","try","tsl","ttl","tts","two","txt","uas","uav","ucr","udp","uml","usc","use","utc","uts","uve","uwb","vdp","vhe","via","vib","vmm","vnf","vsp","vss","vtt","wan","was","way","wdl","why","wit","with","wrt","wsn","xor","yet","zno"]
        
        arrTerm = []
        #rsw = RemoveStopWords('wordcount')
        for term in Lines:
            word_tokens = word_tokenize(term)
            filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words and not w.lower() in customStopWords]
            sentence = " ".join(filtered_sentence)
            arrTerm.append(sentence)

        #    term = rsw.filter_words([term])
        #    if not (len(term)<=2) and term not in customStopWords:
        #        arrTerm.append(term)
        
        
        


        #rsw = RemoveStopWords('wordcount')
        #lines = rsw.read_RDD(filename)
        #filtered_lines = rsw.filter_words(lines)
        #customStopWords = ["aaf","abc","ace","acl","aco","add","aes","afm","aft","ago","aid","aim","aka","all","als","amb","amr","amt","and","ant","any","apd","apl","app","ard","are","ark","arm","ars","art","ash","ast","bal","bar","bid","ble","brt","bsp","but","can","cap","cdc","cdg","cdh","cep","cfd","cfp","cfs","clr","cnf","cod","com","cpg","cps","cqs","csp","ctr","cut","cvs","cwl","cxl","daf","dag","dcs","def","des","dht","dig","diy","dlt","dna","dnn","dos","dot","dpn","dsl","dsm","dsp","due","dve","ecc","ecg","edc","end","eon","epc","esp","etc","etl","fdl","fdn","fed","fee","few","ffc","fhe","fin","for","fsa","gas","gci","gcs","gds","gen","get","gig","gis","gle","gnn","got","gps","gsc","gsp","gui","han","har","hdp","hep","hex","hgn","hoc","how","hrv","hue","icn","ict","ids","ifc","igi","iii","ilp","inâ","inc","ini","inp","iop","ios","ipc","irs","isp","its","ity","jar","jct","jhu","jms","jon","key","kit","kpi","lag","lan","lay","lda","leo","let","lex","lip","liu","llc","lot","lsm","ltd","lxc","may","mbs","mcu","mdc","mdp","mec","met","mfc","mgf","mix","mlr","mme","moe","mom","mpc","mps","mri","muc","ndn","nec","nfn","nft","nfv","ngs","nic","nlp","nmr","non","not","npk","npu","nss","ntt","obe","ocr","oee","ofc","ofn","oil","old","one","ooa","osd","osm","osn","oth","our","out","pcs","pdb","pen","per","pi를","pid","pis","pki","pls","pne","poc","pod","pom","pop","pos","ppg","pro","pss","pte","ptt","put","pvt","qch","qoe","qrp","ran","rar","raw","ray","rfs","rid","rms","rnn","rns","rpa","rps","rrt","rss","rtt","rup","san","sau","say","sba","sbi","scc","sda","sdc","sdi","see","set","sev","sgc","sgd","sgs","sgx","sio","sip","six","sla","slo","smp","snf","sno","snp","sns","soa","soc","sod","sol","sqs","srv","srw","ssd","ssg","ssi","sum","svp","tan","tco","ten","tfc","the","tie","tim","tlb","tls","toa","tor","try","tsl","ttl","tts","two","txt","uas","uav","ucr","udp","uml","usc","use","utc","uts","uve","uwb","vdp","vhe","via","vib","vmm","vnf","vsp","vss","vtt","wan","was","way","wdl","why","wit","with","wrt","wsn","xor","yet","zno"]
        #arrTerm = []
        #for term in filtered_lines:
        #    if not (len(term)<=2) and term not in customStopWords:
        #        arrTerm.append(term)
        
        #for term in arrTerm:
        #    print(term)
        
