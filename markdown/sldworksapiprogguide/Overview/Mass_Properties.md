---
title: "Mass Properties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Mass_Properties.htm"
---

# Mass Properties

The [IMassProperty](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMassProperty.html) object:

- allows applications to directly access individual mass properties as found on the Mass Properties dialog box.
- allows applications to override the following properties as found on the **Override Mass Properties** dialog box:

  - mass
  - center of mass
  - principal axes and principal moments of inertia
  - reference frame and moments of inertia
- obtains mass property information about one or more solid bodies in the document from which the IMassProperty object is obtained.

Only use solid bodies for mass property calculations. You can specify the coordinate system about which the moments are calculated using [IMassProperty::SetCoordinateSystem](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMassProperty~SetCoordinateSystem.html). If you do not use IMassProperty::SetCoordinateSystem, then the document's origin is the coordinate system. By default, system units (meters, radians, and grams) are used. All properties returning a value are adjusted accordingly. See [IMassProperty::UseSystemUnits](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMassProperty~UseSystemUnits.html) for more information.

The results of the mass property calculations vary based on whether or not [IMassProperty::AddBodies](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMassProperty~AddBodies.html) or [IMassProperty::IAddBodies](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMassProperty~IAddBodies.html) is used.

| If IMassProperty::AddBodies or IMassProperty::IAddBodies is... | Then... |
| --- | --- |
| Called and bodies are specified | These bodies can either be from a subset of the document’s body list or from temporary bodies. NOTE: Each specified body should either come from the owning document or be a temporary body. If the body does not satisfy either case, then it is not used when calculating the mass properties. |
| Not called | Mass properties' calculations include all available bodies in the document. Part . All of the solid bodies are included in the calculations. Assembly . All of the bodies in all of the components are used in the calculations. |

If the document from which the IMassProperty object came is an assembly, then any body from any of the child components can be used. When obtaining the body, a call to [IComponent2::GetBodies2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IComponent2~GetBodies2.html) is needed. Your application does not need to make a copy of the body or apply a transform to the body.
