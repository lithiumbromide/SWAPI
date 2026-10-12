---
title: "Callout Property (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "Callout"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Callout.html"
---

# Callout Property (ISelectData)

Gets or sets the callout to attach to the selected object.

## Syntax

### Visual Basic (Declaration)

```vb
Property Callout As Callout
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim value As Callout

instance.Callout = value

value = instance.Callout
```

### C#

```csharp
Callout Callout {get; set;}
```

### C++/CLI

```cpp
property Callout^ Callout {
   Callout^ get();
   void set (    Callout^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Callout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICallout.html) to which to attach the selected object

## VBA Syntax

See [SelectData::Callout](ms-its:sldworksapivb6.chm::/sldworks~SelectData~Callout.html).

## Remarks

This property is not used by [IModelDocExtension::MultiSelect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~MultiSelect.html) or [IModelDocExtension::IMultiSelect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IMultiSelect.html).

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
