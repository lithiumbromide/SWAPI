---
title: "GetProcessID Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetProcessID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetProcessID.html"
---

# GetProcessID Method (ISldWorks)

Gets the process ID for the current SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProcessID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.GetProcessID()
```

### C#

```csharp
System.int GetProcessID()
```

### C++/CLI

```cpp
System.int GetProcessID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Process ID

## VBA Syntax

See [SldWorks::GetProcessID](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetProcessID.html).

## Examples

[Get Process ID of SOLIDWORKS Session (C#)](Get_Process_ID_of_SOLIDWORKS_Session_Example_CSharp.htm)
[Get Process ID of SOLIDWORKS Session (VB.NET)](Get_Process_ID_of_SOLIDWORKS_Session_Example_VBNET.htm)
[Get Process ID of SOLIDWORKS Session (VBA)](Get_Process_ID_of_SOLIDWORKS_Session_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
