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
  <td>192.168.56.102</td>
</tr>
 <tr>
  <td>node-02</td>
  <td>192.168.56.104</td>
</tr>
 <tr>
  <td>monitor</td>
  <td>192.168.56.103</td>
</tr>
</table>

Le bastion peut bien les atteindre en SSH et aucune machine inutile n'a été générée.

## 5. Intégrer Terraform et Ansible

En cas de lancement de la commande 

``` terraform apply ```

Le fichier `generate_hosts.py` va modifier le fichier hosts.ini et ansible va lancer les playbooks.

Le tout fonctionne correctement.