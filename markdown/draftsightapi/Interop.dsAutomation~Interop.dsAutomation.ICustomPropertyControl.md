---
title: "ICustomPropertyControl Interface"
project: ""
interface: "ICustomPropertyControl"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl.html"
---

# ICustomPropertyControl Interface

Allows access to a custom tab.

## Syntax

### Visual Basic

```vb
Public Interface ICustomPropertyControl
```

### C#

```csharp
public interface ICustomPropertyControl
```

### JScript

```
public interface ICustomPropertyControl
```

### Managed Extensions for C++

```
public __gc __interface ICustomPropertyControl
```

### C++/CLI

```cpp
public interface class ICustomPropertyControl
```

## Remarks

You can create your own ActiveX control or Windows form and assign it to a new tab, similar to the DraftSight Properties tab. To assign your form to the new tab, you must call [ICustomPropertyControl::GetHWND](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl~GetHWND.html) to set a parent for your form to a handle.

## Accessors

[IApplication::CreateCustomPropertyControl2](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCustomPropertyControl2.html)

## Access Diagram

DSObjectModel.pdf#CustomPropertyControl

[CustomPropertyControl](DSObjectModel.pdf#CustomPropertyControl)

## See Also

[ICustomPropertyControl Members](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[_ICustomPropertyControlEvents_SizeChangedNotifyEventHandler Delegate](Interop.dsAutomation~Interop.dsAutomation._ICustomPropertyControlEvents_SizeChangedNotifyEventHandler.html)
