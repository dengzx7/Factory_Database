# generate.py
# Generating database random data

import random

# insert into WORKER values('wkxxx', 'XX', int(20,45), sex[M, W], 'Job[A, B, C, D]', workshop)
# insert into PART values('parxxx', float(0-3), int(1-10), warehouse_id, workshop_id)
# insert into PRODUCT values ('proxxx', 'Class[A, B, C, D]', price[20-50], warehouse_id)
# insert into MAKE values ('wk_id', 'par_id', date)
# insert into ASSEMBLE values ('pro_id', 'par_id', date)

warehouse_id = ['wh135', 'wh136', 'wh289', 'wh341', 'wh342']
workshop_id = ['ws063', 'ws064', 'ws077', 'ws079', 'ws147', 'ws148', 'ws169', 'ws265', 'ws266', 'ws498']
classClass = ['ClassA', 'ClassB', 'ClassC', 'ClassD']
alphbat = [chr(65 + i) for i in range(0, 26)]
sexlist = ['M', 'W']
Joblist = ['JobA', 'JobB', 'JobC', 'JobD']
worker_id = ["'wk488'", "'wk639'", "'wk441'", "'wk115'", "'wk374'", "'wk889'", "'wk561'", "'wk867'", "'wk854'", "'wk201'", "'wk737'", "'wk801'", "'wk886'", "'wk788'", "'wk799'", "'wk562'", "'wk979'", "'wk859'", "'wk175'", "'wk862'", "'wk647'", "'wk505'", "'wk957'", "'wk555'", "'wk338'", "'wk795'", "'wk574'", "'wk670'", "'wk132'", "'wk405'", "'wk333'", "'wk493'", "'wk378'", "'wk713'", "'wk245'", "'wk217'", "'wk205'", "'wk718'", "'wk236'", "'wk446'", "'wk168'", "'wk372'", "'wk616'", "'wk121'", "'wk868'", "'wk235'", "'wk916'", "'wk136'", "'wk735'", "'wk147'", "'wk843'", "'wk470'", "'wk471'", "'wk285'", "'wk641'", "'wk124'", "'wk493'", "'wk448'", "'wk417'", "'wk880'", "'wk127'", "'wk801'", "'wk640'", "'wk479'", "'wk910'", "'wk329'", "'wk628'", "'wk805'", "'wk899'", "'wk573'", "'wk673'", "'wk202'", "'wk100'", "'wk962'", "'wk347'", "'wk504'", "'wk188'", "'wk983'", "'wk179'", "'wk490'", "'wk525'", "'wk573'", "'wk588'", "'wk917'", "'wk150'", "'wk337'", "'wk945'", "'wk991'", "'wk502'", "'wk627'", "'wk836'", "'wk219'", "'wk690'", "'wk617'", "'wk522'", "'wk674'", "'wk557'", "'wk942'", "'wk273'", "'wk499'", "'wk796'", "'wk229'", "'wk437'", "'wk367'", "'wk496'", "'wk203'", "'wk517'", "'wk477'", "'wk929'", "'wk337'", "'wk167'", "'wk833'", "'wk653'", "'wk615'", "'wk720'", "'wk504'", "'wk942'", "'wk229'", "'wk133'", "'wk375'", "'wk415'", "'wk697'", "'wk577'", "'wk700'", "'wk981'", "'wk832'", "'wk866'", "'wk719'", "'wk497'", "'wk948'", "'wk796'", "'wk739'", "'wk238'", "'wk122'", "'wk477'", "'wk193'", "'wk278'", "'wk742'", "'wk299'", "'wk339'", "'wk207'", "'wk570'", "'wk755'", "'wk364'", "'wk640'", "'wk675'", "'wk850'", "'wk721'", "'wk809'", "'wk955'", "'wk905'", "'wk361'", "'wk331'", "'wk181'", "'wk757'", "'wk746'", "'wk301'", "'wk626'", "'wk610'", "'wk305'", "'wk947'", "'wk791'", "'wk467'", "'wk388'", "'wk561'", "'wk521'", "'wk111'", "'wk317'", "'wk191'", "'wk234'", "'wk760'", "'wk334'", "'wk617'", "'wk252'", "'wk555'", "'wk620'", "'wk882'", "'wk206'", "'wk973'", "'wk528'", "'wk664'", "'wk738'", "'wk560'", "'wk578'", "'wk157'", "'wk679'", "'wk442'", "'wk606'", "'wk922'", "'wk111'", "'wk684'", "'wk998'", "'wk882'", "'wk672'", "'wk269'", "'wk417'", "'wk900'", "'wk135'", "'wk882'", "'wk542'"]

part_id = ["'par001'", "'par002'", "'par003'", "'par004'", "'par009'", "'par010'", "'par011'", "'par130'", "'par131'", "'par132'", "'par147'", "'par148'", "'par150'", "'par330'", "'par331'", "'par332'", "'par341'", "'par839'", "'par447'", "'par596'", "'par231'", "'par283'", "'par209'", "'par822'", "'par659'", "'par338'", "'par397'", "'par215'", "'par420'", "'par288'", "'par960'", "'par250'", "'par179'", "'par597'", "'par674'", "'par226'", "'par837'", "'par435'", "'par233'", "'par763'", "'par455'", "'par372'", "'par123'", "'par649'", "'par996'", "'par467'", "'par201'", "'par292'", "'par638'", "'par975'", "'par412'", "'par686'", "'par203'", "'par277'", "'par216'", "'par901'", "'par851'", "'par552'", "'par175'", "'par423'", "'par181'", "'par350'", "'par594'", "'par198'", "'par459'", "'par352'", "'par719'", "'par874'", "'par223'", "'par869'", "'par886'", "'par722'", "'par679'", "'par937'", "'par431'", "'par767'", "'par927'", "'par994'", "'par701'", "'par116'", "'par187'", "'par137'", "'par622'", "'par171'", "'par762'", "'par831'", "'par916'", "'par914'", "'par384'", "'par171'", "'par390'", "'par536'", "'par384'", "'par891'", "'par793'", "'par940'", "'par515'", "'par613'", "'par986'", "'par704'", "'par287'", "'par307'", "'par436'", "'par738'", "'par940'", "'par186'", "'par819'", "'par649'", "'par606'", "'par699'", "'par741'", "'par432'", "'par493'", "'par993'", "'par934'", "'par631'"]

product_id = ["'pro003'","'pro004'","'pro005'","'pro045'","'pro046'","'pro050'","'pro063'","'pro064'","'pro100'","'pro130'","'pro140'","'pro151'","'pro152'","'pro153'","'pro154'","'pro172'","'pro179'","'pro252'","'pro270'","'pro342'","'pro361'","'pro388'","'pro401'","'pro460'","'pro462'","'pro498'","'pro510'","'pro568'","'pro616'","'pro625'","'pro627'","'pro651'","'pro661'","'pro683'","'pro692'","'pro700'","'pro709'","'pro714'","'pro867'","'pro871'","'pro900'","'pro908'","'pro911'","'pro923'","'pro966'","'pro984'"]

# ASSEMBLE
# insert into ASSEMBLE values ('pro_id', 'par_id', date)
for k in range(300):
	statement = "insert into ASSEMBLE values ("
	pro_id = random.choice(product_id)
	par_id = random.choice(part_id)
	date = '2018-'
	month = random.randint(1, 12)
	month = str(month)
	day = random.randint(1, 30)
	day = str(day)
	date = "'" + date + month + '-' + day + "'"
	statement += pro_id + ',' + par_id + ',' + date + ')'
	print (statement)

# MAKE
# insert into MAKE values ('wk_id', 'par_id', date)
for k in range(300):
	statement = "insert into MAKE values ("
	wk = random.choice(worker_id)
	par = random.choice(part_id)
	date = '2018-'
	month = random.randint(1, 12)
	month = str(month)
	day = random.randint(1, 30)
	day = str(day)
	date = "'" + date + month + '-' + day + "'"
	statement += wk + ',' + par + ',' + date + ')'
	print (statement)

# worker
worker_id_list = []
for k in range(0, 200):
	statement = "insert into WORKER values ("
	wk_id = "wk"
	wkval = random.randint(100, 999)
	wk_id = "'" + wk_id + str(wkval) + "'"
	name = "'" + random.choice(alphbat) + random.choice(alphbat) + "'"
	age = "'" + str(random.randint(20, 45)) + "'"
	sex = "'" + random.choice(sexlist) + "'"
	job = "'" + random.choice(Joblist) + "'"
	ws = "'" + random.choice(workshop_id) + "'"
	statement += wk_id + ',' + name + ',' + age + ',' + sex + ',' + job + ',' + ws + ')'
	print (statement)
	worker_id_list.append(wk_id)
print (worker_id_list)

# part
part_id_list = []
for k in range(0, 100):
	statement = "insert into PART values ("
	part_id  = "par"
	parval = random.randint(100, 999)
	part_id = "'" + part_id + str(parval) + "'"
	weight = round(3 * random.random(), 1)
	weight = str(weight)
	price = random.randint(1, 10)
	price = str(price)
	wh = random.choice(warehouse_id)
	wh = "'" + wh + "'"
	ws = random.choice(workshop_id)
	ws = "'" + ws + "'"
	statement += part_id + ',' + weight + ',' + price + ',' + wh + ',' + ws + ')'
	print (statement)
	part_id_list.append(part_id)
print (part_id_list)

# product
for k in range(0, 30):
	statement = "insert into PRODUCT values ("
	pro_id  = "pro"
	proval = random.randint(100, 999)
	pro_id = "'" + pro_id + str(proval) + "'"
	classS = "'" + random.choice(classClass) + "'"
	price = random.randint(20, 50)
	price = str(price)
	wh = random.choice(warehouse_id)
	wh = "'" + wh + "'"
	statement += pro_id + ',' + classS + ',' + price + ',' + wh + ')'
	print (statement)
