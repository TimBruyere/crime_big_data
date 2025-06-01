Reponse aux requêtes :

question 1 : MATCH (:Poste)-[r:REPORTED_CRIME {annee: 2021}]->(c:Crime) RETURN c.description AS crime_type, SUM(r.faits) AS total_faits ORDER BY total_faits DESC LIMIT 5

question 2 : MATCH (d:Departement)-[:HAS_PERIMETRE]->(:Perimetre)-[:HAS_POSTE]->(s:Poste)
      -[r:REPORTED_CRIME]->(c:Crime)
WHERE c.description =~ '(?i).vol.'
  AND r.annee = 2021
RETURN d.numero AS departement, SUM(r.faits) AS total_vols
ORDER BY total_vols DESC

question 3 : MATCH (s:Poste {nom: 'SPAFT PREVESSIN'})-[r:REPORTED_CRIME]->(c:Crime)
RETURN s, r, c

Avantage de la visualisation Graphe : 

La visualisation graphe permet de transformer un large panel de données, en noeuds et relation permettant de visualiser les corrélations de données plus efficacement
qu'une base de donnée relationnelle pourrait le faire. 
Pouvoir zoomer et comprendre les liens entre différentes données simplifient les decisions à prendre ainsi que la compréhension pour les personnes non-expertes.
En outre, la visualisation graphe respecte plus le principe de modelisation naturelle en permettant d'incarner le réseau des crimes recensés par la police et gendarmerie nationale en france
que nous avons pu étudier lors de ce TP.
