---
title: "PrintStyle Property (ILayer)"
project: ""
interface: "ILayer"
member: "PrintStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~PrintStyle.html"
---

# PrintStyle Property (ILayer)

Gets or sets the PrintStyle for the Layer.

## Syntax

### Visual Basic

```vb
Property PrintStyle As System.String
```

### C#

```csharp
System.string PrintStyle {get; set;}
```

### JScript

```
function get,set PrintStyle : System.String
```

### Managed Extensions for C++

```
__property System.string* get_PrintStyle();
__property void set_PrintStyle(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ PrintStyle {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the PrintStyle

## Remarks

You can only set the name of a PrintStyle if named PrintStyles are used in the drawing. If color-dependent PrintStyles are used in the drawing, then the PrintStyle is set to **ByColor** and is read only. To determine the type of PrintStyle used in the document:

- call [IDocument::GetCommandOptionString](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html) and specify dsCommandOptionString_e.dsCommandOptionString_GetNmPrnStyl for the Var parameter in a project, macro, or script.
- click **Tools > Options > System OptionsPrinting**, expand **Printing**, expand **Default settings**, and examine **Default type** in the user-interface.

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetPrintStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetPrintStyleInViewport.html)
[ILayerManager::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverride.html)
[ILayerManager::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverrides.html)
[ILayer::SetPrintStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetPrintStyleInViewport.html)

## Availability

DraftSight V1R1.1
