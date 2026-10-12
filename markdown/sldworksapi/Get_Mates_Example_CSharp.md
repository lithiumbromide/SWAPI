---
title: "Get Mates Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mates_Example_CSharp.htm"
---

# Get Mates Example (C#)

This example shows how to get all of the mates (IMate2 and IMateInPlace objects) for all components in an assembly.

```
//----------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\advdrawings\bladed shaft.sldasm.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the components and mates.
// 2. Examine the Immediate window.
//-----------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace GetMatesComponent_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel;
            Component2 swComponent;
            AssemblyDoc swAssembly;
            object[] Components = null;
            object[] Mates = null;
            Mate2 swMate;
            MateInPlace swMateInPlace;
            int numMateEntities = 0;
            int typeOfMate = 0;
            int i = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssembly = (AssemblyDoc)swModel;
            Components = (Object[])swAssembly.GetComponents(false);
            foreach (Object SingleComponent in Components)
            {
                swComponent = (Component2)SingleComponent;
                Debug.Print("Name of component: " + swComponent.Name2);
                Mates = (Object[])swComponent.GetMates();
                if ((Mates != null))
                {
                    foreach (Object SingleMate in Mates)
                    {
                        if (SingleMate is SolidWorks.Interop.sldworks.Mate2)
                        {
                            swMate = (Mate2)SingleMate;
                            typeOfMate = swMate.Type;
                            switch (typeOfMate)
                            {
                                case 0:
                                    Debug.Print(" Mate type: Coincident");
                                    break;
                                case 1:
                                    Debug.Print(" Mate type: Concentric");
                                    break;
                                case 2:
                                    Debug.Print(" Mate type: Perpendicular");
                                    break;
                                case 3:
                                    Debug.Print(" Mate type: Parallel");
                                    break;
                                case 4:
                                    Debug.Print(" Mate type: Tangent");
                                    break;
                                case 5:
                                    Debug.Print(" Mate type: Distance");
                                    break;
                                case 6:
                                    Debug.Print(" Mate type: Angle");
                                    break;
                                case 7:
                                    Debug.Print(" Mate type: Unknown");
                                    break;
                                case 8:
                                    Debug.Print(" Mate type: Symmetric");
                                    break;
                                case 9:
                                    Debug.Print(" Mate type: CAM follower");
                                    break;
                                case 10:
                                    Debug.Print(" Mate type: Gear");
                                    break;
                                case 11:
                                    Debug.Print(" Mate type: Width");
                                    break;
                                case 12:
                                    Debug.Print(" Mate type: Lock to sketch");
                                    break;
                                case 13:
                                    Debug.Print(" Mate type: Rack pinion");
                                    break;
                                case 14:
                                    Debug.Print(" Mate type: Max mates");
                                    break;
                                case 15:
                                    Debug.Print(" Mate type: Path");
                                    break;
                                case 16:
                                    Debug.Print(" Mate type: Lock");
                                    break;
                                case 17:
                                    Debug.Print(" Mate type: Screw");
                                    break;
                                case 18:
                                    Debug.Print(" Mate type: Linear coupler");
                                    break;
                                case 19:
                                    Debug.Print(" Mate type: Universal joint");
                                    break;
                                case 20:
                                    Debug.Print(" Mate type: Coordinate");
                                    break;
                                case 21:
                                    Debug.Print(" Mate type: Slot");
                                    break;
                                case 22:
                                    Debug.Print(" Mate type: Hinge");
                                    //
                                    break;
                                // Add new mate types introduced after SOLIDWORKS 2010 FCS here
                            }
                        }
                        if (SingleMate is SolidWorks.Interop.sldworks.MateInPlace)
                        {
                            swMateInPlace = (MateInPlace)SingleMate;
                            numMateEntities = swMateInPlace.GetMateEntityCount();
                            for (i = 0; i <= numMateEntities - 1; i++)
                            {
                                Debug.Print(" Mate component name: " + swMateInPlace.get_MateComponentName(i));
                                Debug.Print(" Type of Inplace mate entity: " + swMateInPlace.get_MateEntityType(i));
                            }
                            Debug.Print("");
                        }
                    }
                }
                Debug.Print("");
            }
        }
        public SldWorks swApp;
    }
}
```
