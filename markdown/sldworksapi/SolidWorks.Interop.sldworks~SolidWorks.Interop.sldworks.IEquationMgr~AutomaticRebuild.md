---
title: "AutomaticRebuild Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "AutomaticRebuild"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~AutomaticRebuild.html"
---

# AutomaticRebuild Property (IEquationMgr)

Gets or sets whether to automatically rebuild after modifications.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutomaticRebuild As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim value As System.Boolean

instance.AutomaticRebuild = value

value = instance.AutomaticRebuild
```

### C#

```csharp
System.bool AutomaticRebuild {get; set;}
```

### C++/CLI

```cpp
property System.bool AutomaticRebuild {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically rebuild after modifications, false to not

## VBA Syntax

See [EquationMgr::AutomaticRebuild](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~AutomaticRebuild.html).

## Remarks

This property corresponds to the **Automatic rebuild** checkbox in the Manage Equations dialog.

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)
[IEquationMgr::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Equation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
