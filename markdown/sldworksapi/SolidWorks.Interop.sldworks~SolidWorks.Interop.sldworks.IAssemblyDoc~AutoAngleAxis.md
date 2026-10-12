---
title: "AutoAngleAxis Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AutoAngleAxis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoAngleAxis.html"
---

# AutoAngleAxis Method (IAssemblyDoc)

Automatically detect the axis for an angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AutoAngleAxis( _
   ByVal Mate As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Mate As System.Object

instance.AutoAngleAxis(Mate)
```

### C#

```csharp
void AutoAngleAxis(
   System.object Mate
)
```

### C++/CLI

```cpp
void AutoAngleAxis(
   System.Object^ Mate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mate`: [IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)

## VBA Syntax

See [AssemblyDoc::AutoAngleAxis](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AutoAngleAxis.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
