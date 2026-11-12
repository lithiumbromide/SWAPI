---
title: "IAddComponent Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "IAddComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddComponent.html"
---

# IAddComponent Method (IDragOperator)

Adds a component to the list of components to drag.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddComponent( _
   ByVal PComp As Component2, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim PComp As Component2
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.IAddComponent(PComp, AppendFlag)
```

### C#

```csharp
System.bool IAddComponent(
   Component2 PComp,
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool IAddComponent(
   Component2^ PComp,
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PComp`: [Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to add to the list
- `AppendFlag`: True to append the component to the list, false to clear the list before adding the component

### Return Value

True if successful, false for failure; fixed components always return false (see **Remarks**)

## VBA Syntax

See [DragOperator::IAddComponent](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~IAddComponent.html).

## Remarks

Components that are constrained via mates are not considered fixed.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::AddComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddComponent.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
