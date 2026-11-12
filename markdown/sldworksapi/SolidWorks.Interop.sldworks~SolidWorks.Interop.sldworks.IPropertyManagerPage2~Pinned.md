---
title: "Pinned Property (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "Pinned"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Pinned.html"
---

# Pinned Property (IPropertyManagerPage2)

Gets or sets the state of the pushpin on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property Pinned As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim value As System.Boolean

instance.Pinned = value

value = instance.Pinned
```

### C#

```csharp
System.bool Pinned {get; set;}
```

### C++/CLI

```cpp
property System.bool Pinned {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if pushpin is pressed, false if not

## VBA Syntax

See [PropertyManagerPage2::Pinned](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~Pinned.html).

## Remarks

| If the user clicks... | And PropertyManagerPage2::GetPinned is... | Then... |
| --- | --- | --- |
| x | True or false | IPropertyManagerPage2Handler8::OnClose (swPropertyManagerPageClose_Closed) is called, the dialog closes, and IPropertyManagerPage2Handler8::AfterClose is called. |
| check mark | True | IPropertyManagerPage2Handler8::OnClose (swPropertyManagerPageClose_Apply) is called, the dialog is not closed, IPropertyManagerPage2Handler8::AfterClose is not called. |
|  | false | IPropertyManagerPage2Handler8::OnClose (swPropertyManagerPageClose_Okay) is called, the dialog is closed, and IPropertyManagerPage2Handler8::AfterClose is called. |

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
