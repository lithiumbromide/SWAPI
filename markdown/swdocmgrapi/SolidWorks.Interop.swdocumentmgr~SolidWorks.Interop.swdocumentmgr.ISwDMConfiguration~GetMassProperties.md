---
title: "GetMassProperties Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "GetMassProperties"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetMassProperties.html"
---

# GetMassProperties Method (ISwDMConfiguration)

Gets the mass properties, if valid, for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassProperties( _
   ByRef bRet As SwDmMassPropError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim bRet As SwDmMassPropError
Dim value As System.Object

value = instance.GetMassProperties(bRet)
```

### C#

```csharp
System.object GetMassProperties(
   out SwDmMassPropError bRet
)
```

### C++/CLI

```cpp
System.Object^ GetMassProperties(
   [Out] SwDmMassPropError bRet
)
```

### Parameters

- `bRet`: Success or error code as defined by [SwDmMassPropError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmMassPropError.html)

### Return Value

Array of mass properties (see Remarks)

## VBA Syntax

See [SwDMConfiguration::GetMassProperties](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~GetMassProperties.html).

## Remarks

This method only returns data for documents created using SOLIDWORKS 2004 (Version 2500) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

The 13 elements in the array are:

| Element | Description |
| --- | --- |
| [0 2]: | (x, y, z) Center of mass (m) |
| [3]: | Volume (m^3) |
| [4]: | Surface area (m^2) |
| [5] : | Mass (kg) |
| [6]: | momXX (kg*m^2) |
| [7] : | momYY (kg*m^2) |
| [8] : | momZZ (kg*m^2) |
| [9] : | momXY (kg*m^2) |
| [10]: | momZX (kg*m^2) |
| [11]: | momYZ (kg*m^2) |
| [12]: | Include hidden |

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
