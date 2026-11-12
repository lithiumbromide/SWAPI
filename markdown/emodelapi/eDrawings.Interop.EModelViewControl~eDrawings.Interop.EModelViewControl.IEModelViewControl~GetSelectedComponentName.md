---
title: "GetSelectedComponentName Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "GetSelectedComponentName"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~GetSelectedComponentName.html"
---

# GetSelectedComponentName Method (IEModelViewControl)

Gets the name of the selected component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedComponentName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.String

value = instance.GetSelectedComponentName()
```

### C#

```csharp
System.string GetSelectedComponentName()
```

### C++/CLI

```cpp
System.String^ GetSelectedComponentName();
```

### Return Value

Name of the selected component or an empty string if a component is not selected

## VBA Syntax

See [EModelViewControl::GetSelectedComponentName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~GetSelectedComponentName.html).

## Remarks

To select a component, call [IEModelViewControl::SelectByRay](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SelectByRay.html) before calling this method.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentConfigurationName Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)
[IEModelViewControl::ComponentCount Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentCount.html)
[IEModelViewControl::ComponentName Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html)
[IEModelViewControl::ComponentState Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentState.html)
[IEModelViewControl::ComponentTransform Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentTransform.html)

## Availability

eDrawings API 2014 SP0
