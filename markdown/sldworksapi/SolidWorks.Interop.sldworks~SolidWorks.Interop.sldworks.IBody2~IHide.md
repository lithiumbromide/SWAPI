---
title: "IHide Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IHide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IHide.html"
---

# IHide Method (IBody2)

Hides a temporary body using the specified part's context.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IHide( _
   ByVal Part As PartDoc _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Part As PartDoc

instance.IHide(Part)
```

### C#

```csharp
void IHide(
   PartDoc Part
)
```

### C++/CLI

```cpp
void IHide(
   PartDoc^ Part
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Part`: [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html)

## VBA Syntax

See [Body2::IHide](ms-its:sldworksapivb6.chm::/sldworks~Body2~IHide.html).

## Remarks

While SOLIDWORKS is displaying your IBody2 object using [IBody2::Display3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html), you cannot release it explicitly or implicitly. Before releasing or allowing your IBody2 object to be released, you must call this method to prevent it from being displayed.

COM applications should avoid explicitly releasing the IBody2 object by calling IBody2->Release() while it is being displayed by SOLIDWORKS.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::Hide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Hide.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
