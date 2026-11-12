---
title: "AddPipePenetration Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddPipePenetration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipePenetration.html"
---

# AddPipePenetration Method (IAssemblyDoc)

Penetrates the adjacent fitting or pipe with the pipe that ends at the selected sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPipePenetration() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Integer

value = instance.AddPipePenetration()
```

### C#

```csharp
System.int AddPipePenetration()
```

### C++/CLI

```cpp
System.int AddPipePenetration();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Indicates the success or failure of the operation as defined in [swPipingPenetrationStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPipingPenetrationStatus_e.html)

## VBA Syntax

See [AssemblyDoc::AddPipePenetration](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddPipePenetration.html).

## Remarks

If the routing DLL is not available, then COM returns ITF_E_ROUTINGNOTLOADED.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddPipingFitting Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipingFitting.html)

## Availability

SOLIDWORKS 99, datecode 1999207
