## 1. Préparer Terraform

Un dossier terraform a bien été créé.

Le bastion, qui va être notre machine hôte, contient bien : 
- Ansible 
- Terraform
- Python3
- Git
- Vault

#### Définition des futures machines

<table>
 <tr>
  <th>Nom</th>
  <th>Rôle</th>
  <th>CPU</th>
  <th>RAM</th>
  <th>Disque</th>
 </tr>
 <tr>
  <td>node-01</td>
  <td>Exécuter l'agent Sentinel</td>
  <td>1</td>
  <td>256 MiB</td>
  <td>Ubuntu</td>
 </tr>
 <tr>
  <td>node-02</td>
  <td>Exécuter l'agent Sentinel</td>
  <td>1</td>
  <td>256 MiB</td>
  <td>Ubuntu</td>
 </tr>
 <tr>
  <td>monitor</td>
  <td>Superviser et exécuter l'agent</td>
  <td>1</td>
  <td>256 MiB</td>
  <td>Ubuntu</td>
 </tr>
</table>

Le bastion a bien accès à l'environnement VirtualBox.

## 2. Décrire les ressources

On va créer 3 VMs, 2 App nodes et 1 monitoring node.

Chaque VM sera basée sur les mêmes ressources :
- 1 CPU
- 256 MiB de RAM
- Ubuntu sans GUI

Un output de l'adresse IP est prévu avec terraform pour pouvoir l'utiliser a posteriori avec Ansible.

## 3. Planifier la création

Le code est bien indenté, cohérent et un output est présent.

Les ressources vont être crées dans le bon ordre, d'abord les nodes (App et monitoring indifféremment).

## 4. Créer les machines

Les machines apparaissent bien sur VirtualBox et leurs IPs sont notées. :
<table>
 <tr>
  <th>Nom</th>
  <th>IP</th>
</tr>
 <tr>
  <td>node-01</td>
  <td>192.168.56.109</td>
</tr>
 <tr>
  <td>node-02</td>
  <td>192.168.56.108</td>
</tr>
 <tr>
  <td>monitor</td>
  <td>192.168.56.107</td>
</tr>
</table>

Le bastion peut bien les atteindre en SSH et aucune machine inutile n'a été générée.

## 5. Intégrer Terraform et Ansible

En cas de lancement de la commande 

``` terraform apply ```

Le fichier `generate_hosts.py` va modifier le fichier hosts.ini et ansible va lancer les playbooks.

Le tout fonctionne correctement.

## 6. Congifurer Hashi Corp Vault

Nous n'avons pas réussi à implémenter le vault pour la gestion des secrets.

Il n'est pas nécessaire pour les mots de passe, étant donné que l'authentification en ssh se fait par clé privée. Il est en revanche nécessaire pour sécuriser les clés privées ssh.

## 7. Vérifier le déploiement Sentinel

L'agent sentinel est envoyé à chaque App node via ansible.

Le code Ansible crée le service sentinel et le démarre à sa création. Les App Nodes exécutent bien le script `sentinel_agent.py` à intervalle régulier.

Le Monitoring node ne reçoit en revanche pas les logs proprement.

## 8. Vérifier la cohérence de Git

Les fichiers terraform sont bien compris dans Git et versionnés comme le reste.

Les secrets (.tfstate, .tfstate.backup ...) sont bien inclus dans le `.gitignore`.

Les commits ont des noms qui explicitent les changements qui ont eu lieu. Certains changements mineurs ne sont cependant pas toujours mentionnés. Par habitude, tous les commits (et commentaires) sont écrits en anglais.

Il est important que le .tfstate reste secret car il dévoile toutes les informations requises pour la création des serveurs, il peut contenir des informations sensibles (même chiffrées). Il est donc important de le conserver secret.

## 9. Vérification finale et démonstration

L'image disque par défaut de la documentation du provider VirtualBox de Terraform ne donnait pas ses identifiants. Il était donc impossible d'initier la connexion en ssh.

Nous avons dû chercher une autre machine virtuelle en ligne. Celle vers laquelle nous nous sommes tournés est une Ubuntu 15.04, donc difficile à mettre à jour via Ansible. Une fois les quelques manipulations faites à la main (faisables pour la plupart par un script bash, mais pas toujours à cause de certaines entrées utilisateur nécessaires), l'automatisation de la configuration fonctionne.

##### Détail des outils utilisés

- Terraform : Création des éléments nécessaires à l'infrastructure (machines virtuelles pour les App et Monitoring nodes)
- Ansible : Configuration des éléments de l'infrastructure (mise à jour du système, installation des paquets nécessaires, écriture des règles de pare-feu, installation du service sentinel)
- Vault : Sécurisation des secrets (clés privées ssh, mots de passe utilisateur, .tfstate)
- Python Sentinel : Agent d'audit qui s'occupera de récolter les données système et de générer des rapports aux formats `.json` et `.md`, et d'enregistrer des logs sur le succès ou non de sa récolte de données.