---
title: "SetSettingsVar Method (IEdmUser11)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUser11"
member: "SetSettingsVar"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser11~SetSettingsVar.html"
---

# SetSettingsVar Method (IEdmUser11)

Sets the specified user setting.

## Syntax

### Visual Basic

```vb
Sub SetSettingsVar( _
   ByVal eVar As EdmUserSetting, _
   ByVal pbsVal As System.String _
)
```

### C#

```csharp
void SetSettingsVar(
   EdmUserSetting eVar,
   System.string pbsVal
)
```

### C++/CLI

```cpp
void SetSettingsVar(
   EdmUserSetting eVar,
   System.String^ pbsVal
)
```

### Parameters

- `eVar`: User setting as defined by [EdmUserSetting](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserSetting.html)
- `pbsVal`: Value of eVar

## Examples

//Preconditions:

//1. Create a C# console application in Visual Studio.

//2. Add references EPDM.Interop.epdm and EPDM.Interop.EPDMResultCode to the project.

//3. Copy the code below to Program.cs.

//4. Change the namespace to match your project name.

//5. Open the Admin Tool and add a user “A” and a user group “NewGroup”. Add a user to NewGroup.

//6. Ensure that parameters of Login match your vault.

//

//Postconditions:

//1. Open the Admin Tool.

//2. Inspect the settings of user “A” to verify that reference files are not auto-selected to get latest when user A checks out a file.

//3. Inspect the settings of user group “NewGroup” to verify that reference files are auto-selected to get latest when a user in user group NewGroup checks out a file.

//Program.cs:

using System;

using System.Text;

using EPDM.Interop.epdm;

using EPDM.Interop.EPDMResultCode;

namespace project_name

{

class Program

{

static string userName = "Admin";

static string vaultName = "JEB12";

static string updUser = "A";

static string updGroup = "NewGroup";

static void Main(string[] args)

{

StringBuilder sb = new StringBuilder();

try

{

sb.AppendFormat("UserName: {0}", userName).AppendLine();

sb.AppendFormat("VaultName: {0}", vaultName).AppendLine();

IEdmVault11 vault = (IEdmVault11)(new EdmVault5());

if (!vault.**IsLoggedIn**)

vault.**Login**(userName, "password", vaultName);

IEdmUserMgr9 userMgr = (IEdmUserMgr9)vault.**CreateUtility**(EdmUtility.EdmUtil_UserMgr);

var userPos = userMgr.**GetFirstUserPosition**();

while (!userPos.IsNull)

{

IEdmUser11 user = (IEdmUser11)userMgr.**GetNextUser**(userPos);

if (user.Name == updUser)

{

//user.SetSettingsVar(EdmUserSetting.EdmSv_AutoGetLatest, "1");

//user.SetSettingsVar(EdmUserSetting.EdmSv_AutoDelete, "1");

user.**SetSettingsVar**(EdmUserSetting.EdmUSv_AutoGetLatestRefs, "0");

sb.AppendFormat("Settings successfully updated for user {0}", updUser).AppendLine();

break;

}

}

var groupPos = userMgr.**GetFirstUserGroupPosition**();

while (!groupPos.IsNull)

{

IEdmUserGroup9 group = (IEdmUserGroup9)userMgr.**GetNextUserGroup**(groupPos);

if (group.Name == updGroup)

{

group.**SetSettingsVar**(EdmGroupSetting.EdmGSv_AutoGetLatestRefs, "1");

sb.AppendFormat("Settings successfully updated for group {0}", updGroup);

break;

}

}

}

catch (System.Runtime.InteropServices.COMException ex)

{

var errorType = typeof(EdmResultErrorCodes_e);

if (Enum.IsDefined(errorType, ex.ErrorCode))

sb.AppendFormat("Edm error occurred: {0}", Enum.GetName(errorType, ex.ErrorCode)).AppendLine();

else

sb.AppendLine("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);

}

catch (Exception ex)

{

sb.AppendFormat("Error occurred: {0}", ex.Message).AppendLine();

}

Console.WriteLine(sb.ToString());

Console.WriteLine("Please press any key to exit");

Console.ReadKey();

}

}

}

## See Also

[IEdmUser11 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser11.html)
[IEdmUser11 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser11_members.html)

## Availability

SOLIDWORKS PDM Professional 2022
