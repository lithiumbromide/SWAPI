---
title: "TemporaryFixGroup Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "TemporaryFixGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroup.html"
---

# TemporaryFixGroup Method (IAssemblyDoc)

Temporarily fix or group selected components during such operations as drag, move, rotate, etc.

## Syntax

### Visual Basic (Declaration)

```vb
Sub TemporaryFixGroup()
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc

instance.TemporaryFixGroup()
```

### C#

```csharp
void TemporaryFixGroup()
```

### C++/CLI

```cpp
void TemporaryFixGroup();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AssemblyDoc::TemporaryFixGroup](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~TemporaryFixGroup.html).

## Examples

[Temporarily Fix and Group Components (C#)](Temporarily_Fix_and_Group_Components_Example_CSharp.htm)
[Temporarily Fix and Group Components (VB.NET)](Temporarily_Fix_and_Group_Components_Example_VBNET.htm)
[Temporarily Fix and Group Components (VBA)](Temporarily_Fix_and_Group_Components_Example_VB.htm)

## Remarks

Use the following selection marks with [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the components:

- 0 = Components to fix

- 2 = Components to group

Call [IAssemblyDoc::TemporaryFixGroupExit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroupExit.html) to change the components back to floating or ungrouped.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::IsFixed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsFixed.html)
[IAssemblyDoc::FixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FixComponent.html)
[IAssemblyDoc::UnfixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UnfixComponent.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
