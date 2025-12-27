REGION=us-west-2
# change REGION if updated
echo "export REGION=${REGION}" | tee -a ~/.bashrc
VPC_ID=$(aws ec2 describe-vpcs --filters Name=isDefault,Values=true --query "Vpcs[].VpcId" --region ${REGION} | jq -r '.[0]')
echo "export VPC_ID=${VPC_ID}"| tee -a ~/.bashrc
SUBNET_ID=$(aws ec2 describe-subnets --region=${REGION} --filters "Name=availabilityZoneId, Values=usw2-az4" --query 'Subnets[*].SubnetId' | jq -r --arg i $(($RANDOM % 2)) '.[$i|tonumber]')
#change availableity zone id by aws ec2 describe-subnets --region=${REGION}
echo "export SUBNET_ID=${SUBNET_ID}"| tee -a ~/.bashrc
export SSH_KEY=pc-key-$(uuidgen --random | cut -d'-' -f1)-$(date +%F)
echo "export SSH_KEY=${SSH_KEY}" |tee -a ~/.bashrc
aws ec2 create-key-pair --key-name ${SSH_KEY} --query KeyMaterial --output text --region=${REGION} > ~/.ssh/${SSH_KEY}
chmod 400 ~/.ssh/${SSH_KEY}
echo "export CLUSTER_NAME=awsgpu"  | tee -a ~/.bashrc
pcluster create-cluster --cluster-name ${CLUSTER_NAME} --cluster-configuration ${CLUSTER_NAME}.yaml