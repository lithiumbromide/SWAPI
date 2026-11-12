---
title: "UserName Property (ICable)"
project: "SOLIDWORKS Routing API Help"
interface: "ICable"
member: "UserName"
kind: "property"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~UserName.html"
---

# UserName Property (ICable)

Gets or sets the name of the cable.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICable
Dim value As System.String

instance.UserName = value

value = instance.UserName
```

### C#

```csharp
System.string UserName {get; set;}
```

### C++/CLI

```cpp
property System.String^ UserName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the cable

## VBA Syntax

See [Cable::UserName](ms-its:routingapivb6.chm::/SWRoutingLib~Cable~UserName.html).

## Examples

See the [ICable](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable.html) examples.

## Remarks

The cable name is a unique value for each cable, and the same value for each core of the cable.

## See Also

[ICable Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable.html)
[ICable Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable_members.html)

## Availability

SOLIDWORKS Routing 2006 FCS
