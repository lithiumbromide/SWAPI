---
title: "SetComponents Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "SetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetComponents.html"
---

# SetComponents Method (IExplodeStep)

Specifies the components of this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetComponents( _
   ByVal Components As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim Components As System.Object

instance.SetComponents(Components)
```

### C#

```csharp
void SetComponents(
   System.object Components
)
```

### C++/CLI

```cpp
void SetComponents(
   System.Object^ Components
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Components`: Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [ExplodeStep::SetComponents](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~SetComponents.html).

## Remarks

Modifying components during editing of this regular explode step modifies the rotational axis if:

- the rotational axis was not provided during creation,

- and -

- the component to which it referred (the last component in the selection list) was removed during editing.

In that case, a rotational axis using the last selected component in the selection list is created.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
