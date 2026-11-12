---
title: "EnablePushPin Property (ICallout)"
project: "SOLIDWORKS API Help"
interface: "ICallout"
member: "EnablePushPin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout~EnablePushPin.html"
---

# EnablePushPin Property (ICallout)

Gets or sets whether to enable the pushpin for this callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnablePushPin As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICallout
Dim value As System.Boolean

instance.EnablePushPin = value

value = instance.EnablePushPin
```

### C#

```csharp
System.bool EnablePushPin {get; set;}
```

### C++/CLI

```cpp
property System.bool EnablePushPin {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable the callout pushpin, false to disable it

## VBA Syntax

See [Callout::EnablePushPin](ms-its:sldworksapivb6.chm::/sldworks~Callout~EnablePushPin.html).

## Examples

[Create Multi-row Callouts (VBA)](Create_Multi-row_Callouts_Example_VB.htm)

## See Also

[ICallout Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout.html)
[ICallout Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
