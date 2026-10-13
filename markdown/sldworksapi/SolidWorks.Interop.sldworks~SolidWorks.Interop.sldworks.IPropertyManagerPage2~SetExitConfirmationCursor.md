---
title: "SetExitConfirmationCursor Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetExitConfirmationCursor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetExitConfirmationCursor.html"
---

# SetExitConfirmationCursor Method (IPropertyManagerPage2)

Obsolete. Superseded by [IPropertyManagerPage2::SetCursor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~SetCursor.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExitConfirmationCursor( _
   ByVal Enable As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim Enable As System.Boolean

instance.SetExitConfirmationCursor(Enable)
```

### C#

```csharp
void SetExitConfirmationCursor(
   System.bool Enable
)
```

### C++/CLI

```cpp
void SetExitConfirmationCursor(
   System.bool Enable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Enable`: True to enable OK cursor, false to not (see **Remarks**)

## VBA Syntax

See [PropertyManagerPage2::SetExitConfirmationCursor](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetExitConfirmationCursor.html).

## Remarks

This method should only be used if your PropertyManager page has selection lists. For example, this cursor is displayed in the SOLIDWORKS Design user-interface when selecting one or more edges to fillet.

After enabling this cursor, you most likely should not disable it; instead, you should let SOLIDWORKS determine when to disable it. SOLIDWORKS disables this cursor when the cursor has moved even just a bit and replaces it with the cursor appropriate for the operation in progress.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
