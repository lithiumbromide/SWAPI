---
title: "SetSerNoNextCounterVal Method (IEdmSerNoGen8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSerNoGen8"
member: "SetSerNoNextCounterVal"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen8~SetSerNoNextCounterVal.html"
---

# SetSerNoNextCounterVal Method (IEdmSerNoGen8)

Sets the next counter value for the specified serial number generator.

## Syntax

### Visual Basic

```vb
Sub SetSerNoNextCounterVal( _
   ByVal bsSerNoName As System.String, _
   ByVal lNextCounterValue As System.Integer _
)
```

### C#

```csharp
void SetSerNoNextCounterVal(
   System.string bsSerNoName,
   System.int lNextCounterValue
)
```

### C++/CLI

```cpp
void SetSerNoNextCounterVal(
   System.String^ bsSerNoName,
   System.int lNextCounterValue
)
```

### Parameters

- `bsSerNoName`: Name of serial number generator
- `lNextCounterValue`: Next value

## Examples

//Preconditions:

//1. Create a C# console application in Visual Studio.

//2. Add references EPDM.Interop.epdm and EPDM.Interop.EPDMResultCode to the project.

//3. Copy the code below to Program.cs.

//4. Change the namespace to match your project name.

//5. Add a serial number generator called “NSN” using the Admin tool.

//6. Ensure that parameters of Login match your vault.

//

//Postconditions:

//1. Open the Admin Tool.

//2. Observe that the next counter value for the NSN serial number generator is 9.

//Program.cs:

using System;

using System.Linq;

using System.Text;

using EPDM.Interop.epdm;

using EPDM.Interop.EPDMResultCode;

namespace project_name

{

class Program

{

static string userName = "Admin";

static string vaultName = "JEB12";

static string serNoGenName = "NSN";

static int newCounterValue = 9;

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

IEdmSerNoGen7 serNoGen7 = (IEdmSerNoGen7)vault.**CreateUtility**(EdmUtility.EdmUtil_SerNoGen);

string[] names = { };

serNoGen7.**GetSerialNumberNames**(out names);

sb.AppendFormat("Serial number generators present in vault: {0}", String.Join(",", names)).AppendLine();

if (names.Contains(serNoGenName))

{

IEdmSerNoGen8 serNoGen8 = (IEdmSerNoGen8)serNoGen7;

serNoGen8.**SetSerNoNextCounterVal**(serNoGenName, newCounterValue);

sb.AppendFormat("Serial number generator's {0} next counter value set to {1}", serNoGenName, newCounterValue).AppendLine();

}

else

{

sb.AppendFormat("There is no {0} serial number generator present in vault", serNoGenName).AppendLine();

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

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_INVALID_SERIAL_NUMBER_NAME is returned if bsSerNoName is incorrect.
- E_EDM_PERMISSION_DENIED is returned if user does not have "Can update serial numbers" permission.

## See Also

[IEdmSerNoGen8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen8.html)
[IEdmSerNoGen8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoGen8_members.html)

## Availability

SOLIDWORKS PDM Professional 2022
