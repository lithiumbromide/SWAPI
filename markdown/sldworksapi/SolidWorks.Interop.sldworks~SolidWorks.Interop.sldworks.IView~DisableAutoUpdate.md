---
title: "DisableAutoUpdate Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "DisableAutoUpdate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~DisableAutoUpdate.html"
---

# DisableAutoUpdate Property (IView)

Gets or sets whether to disable the automatic update of this view.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisableAutoUpdate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.DisableAutoUpdate = value

value = instance.DisableAutoUpdate
```

### C#

```csharp
System.bool DisableAutoUpdate {get; set;}
```

### C++/CLI

```cpp
property System.bool DisableAutoUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to disable the automatic update, false to not

## VBA Syntax

See [View::DisableAutoUpdate](ms-its:sldworksapivb6.chm::/Sldworks~View~DisableAutoUpdate.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2020 SP5, Revision Number 28.5
