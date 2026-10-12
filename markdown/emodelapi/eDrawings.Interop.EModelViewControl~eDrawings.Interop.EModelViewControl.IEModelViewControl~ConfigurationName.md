---
title: "ConfigurationName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ConfigurationName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationName.html"
---

# ConfigurationName Property (IEModelViewControl)

Gets the name of the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationName( _
   ByVal ConfigurationIndex As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim ConfigurationIndex As System.Integer
Dim value As System.String

value = instance.ConfigurationName(ConfigurationIndex)
```

### C#

```csharp
System.string ConfigurationName(
   System.int ConfigurationIndex
) {get;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get(System.int ConfigurationIndex);
}
```

### Parameters

- `ConfigurationIndex`: Index number of the configuration

### Property Value

Name of configuration

## VBA Syntax

See [EModelViewControl::ConfigurationName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ConfigurationName.html).

## Remarks

Because eDrawings does not support inactive configurations for SOLIDWORKS documents, this property does not get configuration names for a SOLIDWORKS document (.**sldprt**, .**sldasm**, and .**slddrw**). To use configurations in eDrawings, you must use an eDrawings file that was published from SOLIDWORKS.

Before calling this property, call [IEModelViewControl::CurrentConfigurationIndex](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentConfigurationIndex.html) or [IEModelViewControl::ConfigurationCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ConfigurationCount.html) to get a valid value for ConfigurationIndex.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ShowConfiguration](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowConfiguration.html)
[IEModelViewControl::ComponentConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)

## Availability

eDrawings API 2005 SP0
