---
title: "SetDontCutAllInstances Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetDontCutAllInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetDontCutAllInstances.html"
---

# SetDontCutAllInstances Method (IDrSection)

Sets whether all instances of the specified component are uncut in this section view or only in the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDontCutAllInstances( _
   ByVal LpComp As Component, _
   ByVal VbCut As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim LpComp As Component
Dim VbCut As System.Boolean
Dim value As System.Boolean

value = instance.SetDontCutAllInstances(LpComp, VbCut)
```

### C#

```csharp
System.bool SetDontCutAllInstances(
   Component LpComp,
   System.bool VbCut
)
```

### C++/CLI

```cpp
System.bool SetDontCutAllInstances(
   Component^ LpComp,
   System.bool VbCut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LpComp`: Pointer to the [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object
- `VbCut`: True if all instances of the selected component are left uncut, false if only the selected component is left uncut

## VBA Syntax

See [DrSection::SetDontCutAllInstances](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetDontCutAllInstances.html).

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetDontCutAllInstances Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetDontCutAllInstances.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
