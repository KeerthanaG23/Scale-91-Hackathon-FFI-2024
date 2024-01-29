import React from 'react';
import DashboardIcon from "@mui/icons-material/Dashboard";
import InventoryTwoToneIcon from "@mui/icons-material/InventoryTwoTone";
import ShowChartOutlinedIcon from "@mui/icons-material/ShowChartOutlined";
import PaymentsOutlinedIcon from "@mui/icons-material/PaymentsOutlined";
import AccountBalanceTwoToneIcon from "@mui/icons-material/AccountBalanceTwoTone";
import IntegrationInstructionsTwoToneIcon from "@mui/icons-material/IntegrationInstructionsTwoTone";
import NewReleasesTwoToneIcon from "@mui/icons-material/NewReleasesTwoTone";
export const Sidebardata = [
  {
    title: "Dashboard",
    icon: <DashboardIcon />,
    link: "/dashboard",
  },
  {
    title: "Real time stock price",
    icon: <PaymentsOutlinedIcon />,
    link: "/rtsp",
  },
  {
    title: "Stock performance Comparison",
    icon: <InventoryTwoToneIcon />,
    link: "/spc",
  },
  {
    title: "Stock Prediction",
    icon: <ShowChartOutlinedIcon />,
    link: "/forecast",
  },
  {
    title: "Pesonalised investment insights",
    icon: <AccountBalanceTwoToneIcon />,
    link: "/pii",
  },
  {
    // drop down
    title: "Trading Strategy - Economic & Geopolitical factors",
    icon: <NewReleasesTwoToneIcon />,
    link: "/trading",
  },
  {
    title: "Algorithimic Trading",
    icon: <IntegrationInstructionsTwoToneIcon />,
    link: "/at",
  },
];