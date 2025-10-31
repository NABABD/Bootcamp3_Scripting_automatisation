# Nova Sentinel infra

Le projet nova sentinel infra consiste en l'automatisation d'une infrastructure d'audit, de sa conception à son maintien.

### Phase 1 :

Implémenter un script python d'audit qui va récupérer les informations des App nodes et les enregistrer dans des logs.

### Phase 2 :

Utiliser Ansible pour automatiser la configuration des App nodes et du Monitoring node, envoyer les logs des App nodes vers le Monitoring node.

### Phase 3 : 

Utiliser Terraform pour automatiser la création de l'infrastructure et le combiner à Ansible pour automatiser dans la foulée la configuration des machines virtuelles.