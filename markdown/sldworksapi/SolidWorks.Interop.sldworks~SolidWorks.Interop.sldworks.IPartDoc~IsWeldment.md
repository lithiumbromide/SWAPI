---
title: "IsWeldment Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IsWeldment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IsWeldment.html"
---

# IsWeldment Method (IPartDoc)

Gets whether this part contains a weldment feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsWeldment() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Boolean

value = instance.IsWeldment()
```

### C#

```csharp
System.bool IsWeldment()
```

### C++/CLI

```cpp
System.bool IsWeldment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if part contains a weldment feature, false if not

## VBA Syntax

See [PartDoc::IsWeldment](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IsWeldment.html).

## Examples

[Does Part Contain a Weldment Feature (VBA)](Does_Part_Contain_a_Weldment_Feature_Example_VB.htm)

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
