---
title: "ISelectEntity Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ISelectEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISelectEntity.html"
---

# ISelectEntity Method (IView)

Selects an entity in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISelectEntity( _
   ByVal Entity As Entity, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Entity As Entity
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.ISelectEntity(Entity, AppendFlag)
```

### C#

```csharp
System.bool ISelectEntity(
   Entity Entity,
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool ISelectEntity(
   Entity^ Entity,
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)
- `AppendFlag`: True appends the entity to the selection list, false replaces the selection list with the entity

### Return Value

True if the entity was selected, false if not

## VBA Syntax

See [View::ISelectEntity](ms-its:sldworksapivb6.chm::/sldworks~View~ISelectEntity.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::SelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SelectEntity.html)
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
