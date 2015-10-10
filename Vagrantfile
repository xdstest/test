VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network "public_network", ip: "192.168.1.49"
    config.vm.synced_folder ".", "/vagrant"
    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
    config.vm.provision :shell, path: "bootstrap.sh"
end
