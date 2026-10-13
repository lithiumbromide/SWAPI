---
title: "GetScale3 Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetScale3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetScale3.html"
---

# GetScale3 Method (ISketchBlockInstance)

Gets the scale for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetScale3( _
   ByVal Ignoreparentscale As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim Ignoreparentscale As System.Boolean
Dim value As System.Double

value = instance.GetScale3(Ignoreparentscale)
```

### C#

```csharp
System.double GetScale3(
   System.bool Ignoreparentscale
)
```

### C++/CLI

```cpp
System.double GetScale3(
   System.bool Ignoreparentscale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ignoreparentscale`: True to ignore the parent scale, false to not

### Return Value

Scale: 0.0000001 to 500000

## VBA Syntax

See [SketchBlockInstance::GetScale3](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetScale3.html).

## Remarks

Use [ISketchBlockInstance::Scale2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale2.html) to set the scale.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
