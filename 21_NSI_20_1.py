def mini(releve, date):
    rang = 0
    mini = releve[rang]
    for i in range(len(releve)):
        temp = releve[i]
        if temp < mini:
            mini = releve[i]
            rang = i
    return mini, date[rang]


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(mini(t_moy, annees))
