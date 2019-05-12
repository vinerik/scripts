###########
# get_locked_users_from_list.ps1
# Desc: This script will list users thar are lockedOut from a list of users
# Arg1: userlist.txt
# Return value : username, lockedout (True/False)
# Return format: CSV
#####################

# Get user properties 
function GetUser_Propertie($username, $propertie1){
    try {
        $user_info = Get-ADUser $username.trim() -Properties $propertie1
        return $user_info
    }
    catch {
        $user_info = Get-ADUser $username.trim() -Properties $propertie1 -Server SERVER_IP
        return $user_info
    }
    Finally {
        $user_info = "Notfound"
    }
   return $user_info
}

# Main #
$propertie=$args[0]


# From the users list get properties
foreach($line in Get-Content .\userlist.txt) {
        $clean_line=$line.trim()
        # Get the properties from AD
        $propertie_value=GetUser_Propertie "$clean_line" "$propertie"
        # Output to file
        $clean_line,$propertie_value.$propertie -join ',' | Out-File -FilePath .\Output_$propertie  -Append
        
}
