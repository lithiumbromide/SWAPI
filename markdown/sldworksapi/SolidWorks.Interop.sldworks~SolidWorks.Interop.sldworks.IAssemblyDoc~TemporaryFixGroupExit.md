---
title: "TemporaryFixGroupExit Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "TemporaryFixGroupExit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroupExit.html"
---

# TemporaryFixGroupExit Method (IAssemblyDoc)

Changes components that were temporarily fixed or grouped back to floating or ungrouped after such operations as drag, move, rotate, etc.

## Syntax

### Visual Basic (Declaration)

```vb
Sub TemporaryFixGroupExit()
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc

instance.TemporaryFixGroupExit()
```

### C#

```csharp
void TemporaryFixGroupExit()
```

### C++/CLI

```cpp
void TemporaryFixGroupExit();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AssemblyDoc::TemporaryFixGroupExit](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~TemporaryFixGroupExit.html).

## Examples

[Temporarily Fix and Group Components (C#)](Temporarily_Fix_and_Group_Components_Example_CSharp.htm)
[Temporarily Fix and Group Components (VB.NET)](Temporarily_Fix_and_Group_Components_Example_VBNET.htm)
[Temporarily Fix and Group Components (VBA)](Temporarily_Fix_and_Group_Components_Example_VB.htm)

## Remarks

To temporarily change floating or ungrouped components to fixed or grouped, call [IAssemblyDoc::TemporaryFixGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroup.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::IsFixed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsFixed.html)
[IAssemblyDoc::FixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FixComponent.html)
[IAssemblyDoc::UnfixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UnfixComponent.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
