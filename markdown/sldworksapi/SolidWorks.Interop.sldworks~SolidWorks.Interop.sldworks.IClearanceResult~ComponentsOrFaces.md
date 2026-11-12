---
title: "ComponentsOrFaces Property (IClearanceResult)"
project: "SOLIDWORKS API Help"
interface: "IClearanceResult"
member: "ComponentsOrFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ComponentsOrFaces.html"
---

# ComponentsOrFaces Property (IClearanceResult)

Gets the assembly components, faces, or both involved in this clearance result.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentsOrFaces As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceResult
Dim value As System.Object

value = instance.ComponentsOrFaces
```

### C#

```csharp
System.object ComponentsOrFaces {get;}
```

### C++/CLI

```cpp
property System.Object^ ComponentsOrFaces {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of assembly [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)s, [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s, or both

## VBA Syntax

See [ClearanceResult::Components](ms-its:sldworksapivb6.chm::/sldworks~ClearanceResult~Components.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.html)
[IClearanceResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
