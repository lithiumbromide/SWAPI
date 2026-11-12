---
title: "GetArrowHeadInfo Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetArrowHeadInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadInfo.html"
---

# GetArrowHeadInfo Method (ISFSymbol)

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArrowHeadInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim value As System.Object

value = instance.GetArrowHeadInfo()
```

### C#

```csharp
System.object GetArrowHeadInfo()
```

### C++/CLI

```cpp
System.Object^ GetArrowHeadInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles describing format (see **Remarks**)

## VBA Syntax

See [SFSymbol::GetArrowHeadInfo](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetArrowHeadInfo.html).

## Remarks

Format of return information is the following array of doubles:

| retval [0] | = Arrow length (leader into arrowhead) |
| --- | --- |
| retval [1] | = Arrowhead length |
| retval [2] | = Arrowhead width |
| retval [3] | = Arrowhead style as defined in swArrowStyle_e |

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadAtIndex.html)
[ISFSymbol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadCount.html)
[ISFSymbol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadAtIndex.html)
[ISFSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadInfo.html)
