---
title: "GetLineAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLineAtIndex.html"
---

# GetLineAtIndex Method (ISFSymbol)

Gets information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLineAtIndex(Index)
```

### C#

```csharp
System.object GetLineAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLineAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the line where the index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [SFSymbol::GetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetLineAtIndex.html).

## Remarks

Call [ISFSymbol::GetLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetLineCount.html) before calling this method to get the number of lines in this surface finish symbol.

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3] ]

where:

| lineType | = Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | = XYZ line start point |
| endPt [3] | = XYZ line end point |

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetLineAtIndex.html)
