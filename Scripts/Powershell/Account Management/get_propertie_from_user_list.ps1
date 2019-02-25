###########
# get_locked_users_from_list.ps1
# Desc: This script will list users thar are lockedOut from a list of users
# Arg1: userlist.txt
# Return value : username, lockedout (True/False)
# Return format: CSV
#####################

# Get user properties 
function GetUser_Propertie($username, $propertie1){
    $user_info = Get-ADUser $username.trim() -Properties $propertie1
    return $user_info
}

# Main #
$propertie=$args[0]


# From the users list get properties
foreach($line in Get-Content .\userlist.txt) {
        $clean_line=$line.trim()
        # Get the properties from AD
        $propertie_value=GetUser_Propertie "$clean_line" "$propertie"
        write-host $clean_line "," $propertie_value.$propertie
}
