---
title: "ConfigurationCount Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ConfigurationCount"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationCount.html"
---

# ConfigurationCount Property (IEModelViewControl)

Gets the total number of configurations.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

value = instance.ConfigurationCount
```

### C#

```csharp
System.int ConfigurationCount {get;}
```

### C++/CLI

```cpp
property System.int ConfigurationCount {
   System.int get();
}
```

### Property Value

Total number of configurations

## VBA Syntax

See [EModelViewControl::ConfigurationCount](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ConfigurationCount.html).

## Remarks

Because eDrawings does not support inactive configurations for SOLIDWORKS documents, this property does not get the number of configurations in a SOLIDWORKS document (.**sldprt**, .**sldasm**, and .**slddrw**). To use configurations in eDrawings, you must use an eDrawings file that was published from SOLIDWORKS.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationName.html)
[IEModelViewControl::CurrentConfigurationIndex](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentConfigurationIndex.html)
[IEModelViewControl::ShowConfiguration](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowConfiguration.html)
[IEModelViewControl::ComponentConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)

## Availability

eDrawings API 2005 SP0
