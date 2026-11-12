---
title: "GetCommandID Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCommandID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.html"
---

# GetCommandID Method (ISldWorks)

Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., an add-in's toolbar button).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandID( _
   ByVal Clsid As System.String, _
   ByVal UserCmdID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Clsid As System.String
Dim UserCmdID As System.Integer
Dim value As System.Integer

value = instance.GetCommandID(Clsid, UserCmdID)
```

### C#

```csharp
System.int GetCommandID(
   System.string Clsid,
   System.int UserCmdID
)
```

### C++/CLI

```cpp
System.int GetCommandID(
   System.String^ Clsid,
   System.int UserCmdID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Clsid`: Add-in's class ID
- `UserCmdID`: User-defined command ID for the add-in's control (see **Remarks**)

### Return Value

Actual runtime value that SOLIDWORKS assigned the add-in's control

## VBA Syntax

See [SldWorks::GetCommandID](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCommandID.html).

## Remarks

UserCmdId is the same user-defined command ID specified when you created the add-in control using [ICommandGroup::AddCommandItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~AddCommandItem2.html). You need the SOLIDWORKS command ID if you want to do something like cause an add-in's toolbar button to flash when visible in SOLIDWORKS.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ICommandGroup::CommandID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
