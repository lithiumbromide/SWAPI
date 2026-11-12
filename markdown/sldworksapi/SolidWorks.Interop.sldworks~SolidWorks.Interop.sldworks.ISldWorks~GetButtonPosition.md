---
title: "GetButtonPosition Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetButtonPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetButtonPosition.html"
---

# GetButtonPosition Method (ISldWorks)

Gets the center coordinates of the specified SOLIDWORKS toolbar button.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetButtonPosition( _
   ByVal PointAt As System.Integer, _
   ByRef LocX As System.Integer, _
   ByRef LocY As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim PointAt As System.Integer
Dim LocX As System.Integer
Dim LocY As System.Integer
Dim value As System.Boolean

value = instance.GetButtonPosition(PointAt, LocX, LocY)
```

### C#

```csharp
System.bool GetButtonPosition(
   System.int PointAt,
   out System.int LocX,
   out System.int LocY
)
```

### C++/CLI

```cpp
System.bool GetButtonPosition(
   System.int PointAt,
   [Out] System.int LocX,
   [Out] System.int LocY
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointAt`: Command ID for SOLIDWORKS toolbar button as defined in [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.html)
- `LocX`: x coordinate of the center of the specified SOLIDWORKS toolbar button
- `LocY`: y coordinate of the center of the specified SOLIDWORKS toolbar button

### Return Value

True if method call is successful, false if not

## VBA Syntax

See [SldWorks::GetButtonPosition](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetButtonPosition.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddToolbar5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
