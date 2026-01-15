# MLFlow

## Mise en place de Garage

1. Démarrer le service Garage avec Docker Compose :
```shell
docker compose up garage -d
```

2. Vérifier que le service fonctionne :
```shell
docker exec -it garage /garage status
```

Mémoriser l'ID du node retourné. actuellement : b4d76c96a3439da2

3. Assigner un layout :
```shell
docker exec -it garage /garage layout assign -z dc1 -c 1G <node_id>
docker exec -it garage /garage layout apply --version 1
```

4. Créer un bucket de stockage puis vérifier sa création :
```shell
docker exec -it garage /garage bucket create mlflow-bucket
docker exec -it garage /garage bucket info mlflow-bucket
```

5. Créer une key pour le bucket puis l'assigner au bucket en lui donnant les permissions nécessaires :
```shell
docker exec -it garage /garage key create mlflow-key
docker exec -it garage /garage bucket allow --read --write --owner mlflow-bucket --key mlflow-key
```

Mémoriser la valeur de la key retournée (Key ID et Secret key).
KEY ID : GK946043f9ae9c5e813a83ea7a
Secret key ID : 43a41183c17e79d8b7b968a0785a0b3c5728249bd3236893bd9c1ba0495ec842
6. Dans le fichier `mlflow/docker-compose.yaml`, modifier les variables d'environnement `AWS_ACCESS_KEY_ID` et `AWS_SECRET_ACCESS_KEY` pour le service `mlflow` avec les valeurs de la key mémorisées précédemment.

## Démarrer le service MLFlow avec Docker Compose :

Après avoir réaliser les étapes de mise en place de Garage, démarrer le service MLFlow :
```shell
docker compose up -d
```

## Utiliser MLFlow :

L'interface MLFlow est accessible à l'adresse : [http://localhost:5000](http://localhost:5000).

Pour utiliser MLFlow avec Python, installer la bibliothèque :
```shell
pip install mlflow
```